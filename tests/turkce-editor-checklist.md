# Kalemdar 1.2: Türkçe editörlük kontrol örnekleri

Bunlar bir modelin otomatik geçme testleri değildir. Yanıtları incelemek için örnek gözden geçirme senaryolarıdır.

| Girdi | Beklenen düzenleme / kontrol |
|---|---|
| Öğretmenlerde toplantıya katıldı. | 'Öğretmenler de toplantıya katıldı.' bağlaç olan de ayrı |
| Kitap ta masada duruyor. | 'Kitap da masada duruyor.' bağlaçta da/de |
| Dünkü toplantıdaki kararlar... | -ki ekinin ve tamlama zincirinin bağlamda doğru olması |
| Çalışma tamamlandı mı? | soru eki ayrı, soru işareti yerinde |
| Toplantıya Ayşe, ve Ali katıldı. | ve öncesindeki gereksiz virgülü çıkar |
| Katılım azaldı; dolayısıyla başvuru sayısı arttı. | nedensellik kanıtlanmadıysa dolayısıyla'yı sil, iki yargıyı ayrı ver |
| Projenin uygulanmasının gerçekleştirilmesi sağlanacaktır. | verilmiş anlamı koruyarak fiili sadeleştir |
| Bu bağlamda ayrıca öte yandan... | işlevsiz üst üste bağlayıcıları temizle |
| Sonuçlar yöntemin etkiyi kanıtladığını göstermektedir. | bulgular ve yöntem yoksa nedensellik iddiası uydurma |
| Proje kapsamında Yenilikçi Sınıf... | resmî adlarda kelimeyi salt klişe diye değiştirme |
| alıntı, DOI, sayılar ve tarih içeren metin | atıf ve olguları koru; kaynak uydurma |
| İngilizce veya çok dilli metin | Türkçe dil bilgisini yabancı dile dayatma |
| DOCX kurumsal şablon | dil doğruluğunu kontrol et, özgün sayfa yerleşimini koru |

Kapsamlı Türkçe kontrol matrisi: `skills/kalemdar-natural-writing/references/turkce-dil-rehberi.md`.
