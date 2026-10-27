# Kalemdar DOCX tasarım ve doğrulama ilkeleri

## İçerik ve tür

Önce belge türünü ve okuyucunun işi belirle. Akademik belgede yayın benzeri sade
tipografi, proje dosyasında faaliyet/çıktı görünürlüğü, kurumsal raporda ciddi ve
bilgi yoğun düzen, eğitim materyalinde yaşa uygun okunabilirlik ve çalışma alanı
kur. Her belgenin aynı tasarımla üretilmesini önle. Belge içinde tutarlı kal.
Kullanıcı çalışma kâğıdı için Poppins belirttiyse onu koru; kurum/yayın şablonunun
zorunlu fontunu başka bir belgede keyfî olarak Poppins'e dönüştürme.

## Şablona sadakat

Verilen DOCX'i yerinde temel al. Sayfa boyutunu, yönünü, bölüm yapısını, margin
değerlerini, header/footer'ı, logo konumunu, stilleri ve tablo geometrisini koru.
Yeni içeriği bu sisteme yerleştir. Gerekirse aynı sayfayı çoğalt. Taşmayı çözmek
için kenar boşluklarını rastgele daraltma, bütün yazıları küçültme veya şablonu
yeniden tasarlama. Kaynak şablonla karşılaştırarak metin kaymalarını kontrol et.

## Tablo ve sayfa düzeni

- Yalnızca gerçekten satır/sütun ilişkisi taşıyan bilgiyi tabloya koy. Düz metni
  sırf hizalamak için sürekli tabloya çevirme.
- Tablo içeriği birden fazla sayfa gerektiriyorsa **her sayfada ayrı ve bağımsız
  tablo oluştur**. Tek bir uzun tabloyu sayfalar boyunca devam ettirme. Mantıksal
  gruplara böl, başlık satırını her tabloda yinele ve araya gerçek sayfa sonu koy.
  Tablo içermeyen sayfalara gereksiz tablo ekleme.
- Bir sayfayı aşan tabloyu gerçek render sonucuna göre daha küçük bağımsız
  tablolara ayır. Çok uzun bir açıklamayı bölümle; okunabilirliği bozacak kadar
  küçültme. Satırların iki sayfaya bölünmesini önle. `cantSplit` tek başına bir
  tablonun tek sayfada kaldığını kanıtlamaz, sayfa görüntülerini de incele.
- Açıklama sütunlarını geniş, tarih/kod/sayı alanlarını dar kur. Sütunları otomatik
  olarak eşitleme. Hücre iç boşluklarını, dikey hizayı ve toplam kullanılabilir
  genişliği denetle. İçeriği hücreye sıkıştırma.
- İşleve göre veri tablosunu yoğun ve sade, plan tablosunu açıklamaya elverişli,
  değerlendirmeyi puanlamaya uygun, takvimi tarih odaklı, karşılaştırmayı kolay
  taranabilir düzenle. Sırf çeşitlilik olsun diye farklı stiller ekleme.

## Görünüm

Bir ana font ve gerçekten gerekiyorsa bir tamamlayıcı kullan. Genellikle ana
başlık, bölüm ve alt başlık olmak üzere üç hiyerarşi seviyesi yeterli olsun.
Hiyerarşiyi önce punto, ağırlık, hizalama, satır aralığı ve boşlukla göster.
Gerçek Word başlık/paragraf stillerini, listeleri, tabloları, sayfa ve bölüm
sonlarını kullan. Boşluk veya tab karakterleriyle sahte hizalama yapma.

Yeni bir belge için varsayılan lacivert/mavi başlıklar, gri/mavi tablo dolguları,
renkli kutular, kalın çerçeveler, aynı kart yapısı, yatay çizgiler, WordArt,
dekoratif şekiller, degrade/gölge, tümü büyük harf başlıklar ve her alt başlıkta
numara kullanma. Kullanıcının sağladığı şablonda bunlar varsa şablonu koru.

Nötr ve kontrollü bir renk sistemi kullan. Verilen kurumsal rengi sınırlı vurgu
olarak uygula. Bütün başlık, kutu, çizgi ve tabloları aynı renge boyama. Kullanıcı
istemeden gökkuşağı veya yan yana gökkuşağı renkleri kullanma.

Ampul, hedef, roket, büyüteç, yapboz, el sıkışma, dünya ve grafik oku ikonlarını
başlıklara kendiliğinden ekleme. Kullanıcı ikon istemedikçe ekleme. Görseli bilgi,
bağlam veya gerçek belge ihtiyacı için kullan, sayfayı doldurmak için stok görsel
ekleme. Kesin veriyi gösteren grafikleri veya şemaları doğru veriyle oluştur.
Görsellerin en-boy oranını koru. Kullanıcının logo/kimliğini yeniden üretme.

Bilgi kutusunu ayrı tutulması gereken yöntem özeti, kritik not, gösterge veya
uyarıyla sınırla. Her paragrafı kutuya alma. Renkli header, büyük logo alanı veya
dekoratif footer'ı otomatik ekleme. Mevcut kurumsal kimliği izle.

## Boşluk ve son kontrol

Başlıktan önce ve sonra işlevine uygun boşluk kullan. Paragraf boşluğunu mekanik
biçimde her öğede eşitleme, devasa aralıklar veya tek metin bloğu oluşturma.
Sayfayı zorla tamamen doldurma ve gereksiz büyük boş alanlar bırakma. Başlık/alt
başlığı sayfa sonunda yalnız bırakma. Tablo başlığıyla tabloyu, kısa paragrafla
devamını birlikte tut. Dul/yetim satırları, kırpılan metni ve boş sayfaları düzelt.

Standart `.docx`/OOXML üret. RTF, Visual Basic, VBA/makro kullanma. Dosya uzantısını
değiştirerek sahte DOCX yapma. İçeriği dosyaya aktarırken tam metni koru.

Yerel yardımcıyla dosya yapısını incele, ancak XML çıktısını görsel doğrulama
yerine geçirme. Ortamda kullanılabilir bir Word/DOCX render aracı varsa belgeyi
render et ve **her sayfayı** incele. Oluşturulan PDF'deki sayfa sayısı ve görüntüleri
gerçek yerleşim doğrulamasıdır. DOCX içindeki `Pages` meta değeri eski olabilir.
Render aracı yoksa bu sınırlılığı kısa ve açık bildir, görsel kontrol yapılmış gibi
sunma. Dosya üretim aracı yoksa yalnızca hazır içerik sun, olmayan dosyaya link verme.

Teslim kontrolü: şablon geometrisi korunmuş mu, çok sayfalı tablolar bağımsız mı,
satır ve başlık taşması var mı, sütunlar işlevine uygun mu, metin sıkışmış mı,
gereksiz mavi/gri dolgu/kutu/ikon/degrade/gölge kalmış mı, gerçek bilgiler ve metin
tam mı, dosya açılıyor mu? Sorunları düzelt, sonra ortamın dosya kaydetme ve teslim
kurallarına göre gerçek dosyayı sun. Tasarımın içeriği okuma ve kullanmayı destekle.

## Çok dilli metin ve tipografi

Metnin dil ve bölgesel varyantını [çok dilli rehberde](multilingual-style.md) belirle.
Kaynak şablonun fontunu, punto sistemini, sayfa geometrisini ve stillerini koru.
Mevcut font hedef karakter setini desteklemiyorsa şablona zarar vermeden uygun
Unicode font/fallback seçimini değerlendir; fontun gerçekten sistemde bulunup
bulunmadığını doğrula. Sağdan sola alfabelerde Word'ün RTL paragraf yönünü,
karma yönlü metni (sayılar, bağlantılar) ve başlık hizalamasını test et. CJK
metinlerinde satır sonu kırılmaları, noktalama ve karakter sıkışmasını render ederek
incele. Otomatik çeviri veya transliterasyon yapma.
