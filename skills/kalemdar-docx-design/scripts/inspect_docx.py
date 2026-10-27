#!/usr/bin/env python3
"""Inspect DOCX structure with the Python standard library; never claim layout validation."""
import argparse
import hashlib
import json
from pathlib import Path
import sys
from zipfile import BadZipFile, ZipFile
import xml.etree.ElementTree as ET

W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
R = '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}'
APP = '{http://schemas.openxmlformats.org/officeDocument/2006/extended-properties}'

def attr(element):
    if element is None:
        return None
    return {k.rsplit('}', 1)[-1]:v for k, v in element.attrib.items()}

def enabled(element):
    return element is not None and element.get(W+'val', 'true').lower() not in {'0', 'false', 'off'}

def fingerprint(path):
    path = Path(path)
    with ZipFile(path) as z:
        names = z.namelist()
        if len(names) != len(set(names)):
            raise ValueError('Duplicate ZIP entries')
        required = ['[Content_Types].xml', 'word/document.xml']
        for name in required:
            if name not in names:
                raise ValueError(f'Missing DOCX part: {name}')
        bad = z.testzip()
        if bad:
            raise ValueError(f'Corrupt ZIP entry: {bad}')
        doc = ET.fromstring(z.read('word/document.xml'))
        body = doc.find(W+'body')
        if body is None:
            raise ValueError('Missing Word document body')
        sections = []
        for section in doc.iter(W+'sectPr'):
            sections.append({
                'page_size_twips':attr(section.find(W+'pgSz')),
                'margins_twips':attr(section.find(W+'pgMar')),
                'columns':attr(section.find(W+'cols')),
                'header_footer_refs':[{'kind':x.tag.rsplit('}', 1)[-1], **attr(x)}
                                      for x in section if x.tag in [W+'headerReference', W+'footerReference']]
            })
        tables = []
        for ti, table in enumerate(doc.iter(W+'tbl')):
            rows = table.findall(W+'tr')
            props = table.find(W+'tblPr')
            no_split = [i+1 for i, row in enumerate(rows)
                        if enabled(row.find(W+'trPr/'+W+'cantSplit'))]
            tables.append({
                'index':ti+1, 'rows':len(rows),
                'cells_per_row':[len(row.findall(W+'tc')) for row in rows],
                'grid_widths_twips':[x.get(W+'w') for x in table.findall(W+'tblGrid/'+W+'gridCol')],
                'table_width':attr(props.find(W+'tblW')) if props is not None else None,
                'cell_widths':[[attr(c.find(W+'tcPr/'+W+'tcW')) for c in row.findall(W+'tc')] for row in rows],
                'rows_with_no_split':no_split,
                'repeat_header_rows':[i+1 for i, row in enumerate(rows)
                                      if enabled(row.find(W+'trPr/'+W+'tblHeader'))],
                'render_required':True
            })
        styles = []
        if 'word/styles.xml' in names:
            sdoc = ET.fromstring(z.read('word/styles.xml'))
            for s in sdoc.findall(W+'style'):
                rp = s.find(W+'rPr')
                pp = s.find(W+'pPr')
                styles.append({'id':s.get(W+'styleId'), 'type':s.get(W+'type'),
                               'name':attr(s.find(W+'name')),
                               'fonts':attr(rp.find(W+'rFonts')) if rp is not None else None,
                               'font_size_half_points':attr(rp.find(W+'sz')) if rp is not None else None,
                               'color':attr(rp.find(W+'color')) if rp is not None else None,
                               'spacing':attr(pp.find(W+'spacing')) if pp is not None else None})
        reported_pages = None
        if 'docProps/app.xml' in names:
            app = ET.fromstring(z.read('docProps/app.xml'))
            pages = app.find(APP+'Pages')
            reported_pages = pages.text if pages is not None else None
        ctype = z.read('[Content_Types].xml').decode('utf-8')
        macros = [n for n in names if 'vbaproject' in n.lower() or 'vbadata' in n.lower()]
        macro_enabled = 'macroenabled' in ctype.lower()
        hf = {n:hashlib.sha256(z.read(n)).hexdigest() for n in names
              if n.startswith(('word/header', 'word/footer')) and n.endswith('.xml')}
        text = '\n'.join(''.join(t.text or '' for t in p.iter(W+'t')) for p in body.iter(W+'p'))
        warnings = []
        if macros or macro_enabled:
            warnings.append('Macro-bearing package is prohibited')
        for t in tables:
            if len(t['rows_with_no_split']) < t['rows']:
                warnings.append(f'Table {t["index"]}: one or more rows do not set cantSplit; inspect rendered pages')
        page_breaks = sum(x.get(W+'type') == 'page' for x in doc.iter(W+'br'))
        before_breaks = len(list(doc.iter(W+'pageBreakBefore')))
        return {'file':str(path.resolve()), 'sections':sections, 'tables':tables,
                'styles':styles, 'header_footer_hashes':hf, 'text_characters':len(text),
                'explicit_page_breaks':page_breaks, 'page_break_before_properties':before_breaks,
                'inline_or_anchored_drawings':len(list(doc.iter(W+'drawing'))),
                'reported_pages_metadata_may_be_stale':reported_pages,
                'macro_parts':macros, 'macro_enabled_content_type':macro_enabled,
                'warnings':warnings, 'layout_verified':False,
                'layout_note':'Render and inspect every page to verify table independence, overflow and placement.'}

def compare(actual, template):
    dimensions = lambda report:[{k:v for k,v in sec.items() if k != 'header_footer_refs'} for sec in report['sections']]
    geometry = lambda report:[{k:t[k] for k in ['grid_widths_twips','table_width','cell_widths','cells_per_row']} for t in report['tables']]
    return {'page_geometry_equal':dimensions(actual) == dimensions(template),
            'header_footer_xml_equal':actual['header_footer_hashes'] == template['header_footer_hashes'],
            'table_geometry_equal':geometry(actual) == geometry(template),
            'review_note':'Review differences against authorized edits; added pages/tables may change counts legitimately.'}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('document')
    parser.add_argument('--template')
    parser.add_argument('--strict', action='store_true', help='Fail for corrupt DOCX or macro content; does not certify layout')
    args = parser.parse_args()
    try:
        report = fingerprint(args.document)
        if args.template:
            report['template_comparison'] = compare(report, fingerprint(args.template))
        print(json.dumps(report, ensure_ascii=False, indent=2))
        if args.strict and (report['macro_parts'] or report['macro_enabled_content_type']):
            return 2
        return 0
    except (OSError, ValueError, BadZipFile, ET.ParseError) as e:
        print(json.dumps({'error':str(e), 'layout_verified':False}, ensure_ascii=False))
        return 2

if __name__ == '__main__':
    sys.exit(main())
