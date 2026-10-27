---
name: kalemdar-docx-design
description: "Kalemdar ile Word/DOCX belgesi oluştur veya düzenle; sayfa düzeni, tipografi, başlık, tablo, görsel, header/footer ve verilen şablonu koru. Akademik belge, proje dosyası, kurumsal rapor veya eğitim materyalinin Word tesliminde ilgili yazım becerisiyle birlikte kullan. Çok sayfalı tabloları bağımsız sayfa tablolarına ayır."
---

# DOCX Document Design & Formatting

Önce [ortak yazım kurallarını](references/shared-style.md),
[çok dilli yazım rehberini](references/multilingual-style.md) ve
[DOCX tasarım ilkelerini](references/docx-design.md) oku; üçünü birlikte uygula.
Belgenin dili veya yazı sistemi farklıysa dilin tipografik gereksinimlerini
şablonu bozmadan uygula.
Metni nihai kullanımına uygun Kalemdar yazım becerisiyle düzenle. DOCX tasarımını
metnin amacı ve kullanıcının şablonuyla eşleştir.

## İş akışı

1. Sağlanan DOCX/şablonu, metni, sayfa gereksinimlerini ve kurum/yayın kimliğini
   incele. Şablon varsa sıfırdan benzerini üretmek yerine onu temel al.
2. Yerel Python varsa başlangıç yapısını şu yardımcıyla çıkar:
   `python3 scripts/inspect_docx.py TEMPLATE.docx`.
   Sayfa ölçüsü/margin, stiller, tablo geometrisi ve header/footer değerlerini sakla.
3. Belge türüne göre tasarımı seç. Metni gerekli yerlerde gerçek Word yapılarıyla
   yerleştir. Standart DOCX kullan, RTF/VB/VBA/makro kullanma. İçeriği dekoratif
   kartlara dönüştürme. Kullanıcı istemeden ikon veya gökkuşağı ekleme.
4. Çok sayfalı tablo gerekiyorsa her sayfa için ayrı tablo oluştur, başlıkları
   yinele, satırların bölünmesini önle ve gerçek sayfa sonu koy. Tek uzun tabloyu
   sayfalar boyunca sürdürme. Açıklama sütunları ve tablo işlevine göre genişlik kur.
5. Ortamda mevcut DOCX üretim/düzenleme araçlarıyla gerçek dosyayı oluştur.
   Gerekirse `python-docx`, `docx`/OOXML veya mevcut yerel belge araçlarını kullan.
   Bunlar eklentinin sunduğu bir sunucu veya harici hizmet değildir.
6. Yapısal kontrolü çalıştır:
   `python3 scripts/inspect_docx.py OUTPUT.docx --template TEMPLATE.docx --strict`.
   Yeni belgede `--template` parametresini çıkar. JSON'daki uyarıları değerlendir,
   izinli sayfa çoğaltmayla ilgisiz geometri değişikliklerini ayır. Bu yardımcı
   makro/ZIP/XML yapısını denetler, sayfa yerleşimini garanti etmez.
7. Kullanılabilir render aracı varsa tüm sayfaları görsel olarak incele. Şablon
   kayması, metin taşması, başlık yalnızlığı, bağımsız tablolar, görsel oranları,
   gereksiz boş sayfa, okunabilirlik ve renk/ikon tekrarını denetle. Gerekirse düzelt.
8. Gerçek dosyayı ortamın kalıcı kaydetme ve dosya teslim kurallarına göre sun.
   Görsel kontrol yapılamadıysa kısaca belirt. Araç yoksa dosya varmış gibi davranma.

Sayfa düzenini değiştirerek iyi yazılmamış içeriği örtme. Kullanıcının şablonuna
sadakati varsayılan tasarım tercihlerinden önce tut.
