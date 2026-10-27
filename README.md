# Kalemdar v1.1.0

Doğal, somut ve kaynak disiplinini koruyan akademik, proje ve profesyonel yazım için beş beceri. v1.1.0, Türkçe kuralları koruyarak dile ve bölgesel kullanıma özgü editoryal rehberler ekler.

## Türkçe

### Beceriler

| Klasör | Kullanım |
| --- | --- |
| `skills/kalemdar-academic-writing` | Makale, tez, araştırma ve bilimsel rapor |
| `skills/kalemdar-project-writing` | Proje ve hibe başvuruları |
| `skills/kalemdar-essay-writing` | Entelektüel deneme ve eleştirel düşünce yazıları |
| `skills/kalemdar-natural-writing` | Genel, teknik, kurumsal ve profesyonel metin |
| `skills/kalemdar-docx-design` | Word/DOCX düzeni, şablon ve yapısal kontrol |

### Çok dilli kapsam

Türkçe, İngilizce, Almanca, Fransızca, İspanyolca, Portekizce, İtalyanca, Felemenkçe, Lehçe, Rusça, Arapça, Çince, Japonca, Korece ve Hintçe için 15 dil profili bulunur. Rehber; bölgesel varyant, hitap, noktalama, yazı sistemi ve akademik anlatım farklarını ele alır. Açıkça çeviri istenmedikçe kaynak dil korunur. Diğer diller için temkinli düzenleme ilkeleri de vardır.

Bu kapsam, talimatların içeriğini tanımlar. Bütün dillerde eşit kalite, anadili düzeyi veya kapsamlı gerçek kullanım testi yapıldığı anlamına gelmez. Sonuç, kullanılan modelin dil yeteneğine ve sağlanan bağlama bağlıdır.

### Kullanım

Paket, `SKILL.md` dosyalarını ve referanslarını okuyabilen uyumlu bir yapay zekâ/ajan ortamı içindir. Eklenti olarak kullanırken kökteki `plugin.json`, `.codex-plugin/plugin.json`, `assets/` ve `skills/` yapısını birlikte koruyun. Tek bir beceriyi kullanacaksanız kendi klasöründeki `agents/`, `references/` ve varsa `scripts/` dosyalarını da birlikte taşıyın. Kurulum yöntemi kullandığınız istemciye bağlıdır.

Örnek istekler:

- “Bu makale taslağını kaynakları ve iddia gücünü koruyarak düzenle.”
- “Proje başvurusunun ihtiyaç, faaliyet ve ölçüm ilişkisini netleştir; veri uydurma.”
- “Edit this text in British English and preserve the author's voice.”
- “Bu raporu verilen DOCX şablonuna göre düzenle ve sayfa yerleşimini kontrol et.”

Kalemdar harici sunucu, API anahtarı veya ücretli servis bağlantısı içermez. Modeli çalıştıran ortamın kendi koşulları geçerlidir. DOCX üretimi ve sayfa görüntüleme, ortamda mevcut belge araçlarını gerektirir.

DOCX yardımcı betiği Python 3 standart kütüphanesini kullanır:

```bash
python3 skills/kalemdar-docx-design/scripts/inspect_docx.py DOCUMENT.docx --strict
```

Bu betik ZIP/XML yapısını, tablo ve sayfa özelliklerini inceler; gerçek sayfa görüntüsünü doğrulamaz. `--template TEMPLATE.docx` ile şablon yapısı karşılaştırılabilir. Belge görsel olarak incelenmediyse yerleşim doğrulanmış sayılmaz.

### Kaynak yapısı ve güvenlik

Her beceride `SKILL.md`, `agents/openai.yaml`, ortak stil ve çok dilli stil referansları bulunur. DOCX becerisi ek tasarım rehberi ve inceleme betiğini içerir. Ayrıntılar için [CHANGELOG](CHANGELOG.md) ve [SECURITY](SECURITY.md) dosyalarına bakın.

Bu depoda açık bir kullanım lisansı tanımlanmamıştır. Deponun herkese açık olması tek başına yeniden kullanım için lisans verildiği anlamına gelmez.

## English

Kalemdar is a collection of five writing skills for academic work, project and grant proposals, essays, professional text, and DOCX design. It aims to preserve facts, evidence, citations and the author's voice while reducing formulaic prose.

Version 1.1.0 adds 15 language profiles: Turkish, English, German, French, Spanish, Portuguese, Italian, Dutch, Polish, Russian, Arabic, Chinese, Japanese, Korean and Hindi. Guidance covers regional variants, register, punctuation, writing systems and academic conventions. The source language is preserved unless translation is explicitly requested. Coverage describes the instructions; it is not a claim of equal quality or comprehensive testing across all languages.

Use the package in a compatible agent environment that can load `SKILL.md` and its references. Preserve the manifest, asset and skill directory structure. Installation depends on the host client. The package includes no external server, API key or paid service integration. The host model's own terms and costs still apply. DOCX generation and rendering require tools available in the host environment.

The Python standard-library DOCX inspector checks document structure, not rendered layout. See the command above; add `--template TEMPLATE.docx` to compare against a template. See [SECURITY](SECURITY.md) before handling private documents. No explicit reuse license has been assigned in this repository.
