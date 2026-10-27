# Security / Güvenlik

## Kapsam

Kalemdar; metin yönergeleri, görsel varlık ve yerel DOCX inceleme betiğinden oluşur. Paket harici sunucu, API anahtarı, erişim tokenı, kimlik doğrulama akışı veya ücretli servis bağlantısı içermez. Yapay zekâ modelinin çalıştığı ortamın erişim, veri işleme ve ücretlendirme koşulları ayrıca geçerlidir.

## Gizli bilgiler ve özel belgeler

- API anahtarı, token, parola, özel anahtar, `.env` veya kimlik bilgisi dosyalarını depoya, issue'ya, sürüm varlıklarına ya da örnek istemlere eklemeyin.
- Özel belgelerdeki kişisel, kurumsal veya gizli bilgileri herkese açık örneklere taşımayın. Gerekirse anonimleştirilmiş ve sentetik örnek kullanın.
- Şüpheli bir anahtarın yayımlandığını fark ederseniz ilgili servis üzerinden iptal edin veya yenileyin. Dosyayı silmek Git geçmişindeki kopyayı ortadan kaldırmaz.
- `.gitignore` kazara eklemeleri azaltır; gizli bilgi taramasının yerine geçmez. Yayın öncesinde eklenen bütün dosyaları inceleyin.

## DOCX dosyaları

`inspect_docx.py` yerel dosyaların ZIP/XML içeriğini okur. Ağ isteği göndermez ve makro çalıştırmaz. `--strict`, bozuk belge veya tespit edilen makro içeriğinde başarısız olur; belgeyi kötü amaçlı içeriğe karşı sertifikalandırmaz ve sayfa düzenini görsel olarak doğrulamaz.

Güvenilmeyen veya çok büyük DOCX dosyalarını kaynak sınırları olan bir ortamda inceleyin. Hassas dosyaları paylaşmadan önce metni ve belge meta verilerini ayrıca gözden geçirin. Yönergeler bir güvenlik sınırı değildir; kullanılan ajan ortamının izinleri ve araçları belirleyicidir.

## Sorun bildirme

Genel sorunları hassas veri içermeyen, mümkünse sentetik bir örnekle bildirin. Kimlik bilgilerini ve özel belge içeriğini herkese açık bir issue'ya koymayın. Güvenlik sorunu için GitHub'ın özel güvenlik bildirimi özelliği depoda etkinse onu kullanın; etkin değilse depo sahibinden yalnızca güvenli bir özel iletişim kanalı isteyin. Etkin bir özel kanal varmış gibi varsaymayın.

## English

Kalemdar contains instructions, an image asset and a local DOCX inspection script. It includes no server, credentials, authentication flow or paid API integration. The host environment's own privacy, permissions and billing conditions still apply.

Do not commit credentials, private documents or personal information. Review every file before publishing; `.gitignore` is not a secret scanner. Revoke any exposed credential at its provider, since deleting a file does not remove Git history.

The DOCX inspector reads local ZIP/XML data without making network requests or running macros. It does not certify a document as safe or validate rendered layout. Inspect untrusted or large files with resource limits. Report problems using synthetic examples and a private security channel when one is available; never post credentials or private documents in public issues.
