#  🚌 Otobüs Rezervasyon Sistemi

Bu proje, Python dili kullanılarak geliştirilmiş konsol tabanlı bir Otobüs Koltuk Rezervasyon Sistemidir. Kullanıcılar, boş koltukları görebilir, belirli koltuklara rezervasyon yapabilir, yolcu bilgilerini görüntüleyebilir ve sistem üzerinden interaktif bir şekilde işlemlerini gerçekleştirebilir.

##  📌 Özellikler
-  Yolcu bilgileri (Ad, Soyad, Cinsiyet) alınarak koltuk rezervasyonu yapılabilir.

-  Rezerve edilmiş koltuklar tekrar seçilemez, sistem kullanıcıyı uyarır.

-  Tüm yolcular ve tüm koltuklar detaylı şekilde listelenebilir.

-  Sadece boş koltuklar görüntülenebilir.

-  Koltuk numaraları 1-42 arasındadır.

-  0 numaralı koltuk şoför koltuğu olarak ayrılmıştır ve rezerve edilemez.

##  📁 Proje Yapısı
-  Yolcu: Yolcu nesnesini temsil eder.

-  Koltuk: Her bir koltuk için durum, numara ve yolcu bilgilerini barındırır.

-  Otobus: Koltukları yönetir ve yolcu rezervasyonlarını gerçekleştirir.

-  main(): Ana menüyü gösterir ve kullanıcıdan giriş alarak işlemleri yürütür.


##  ▶️ Kullanım
Programı çalıştırdıktan sonra aşağıdaki menüyle karşılaşırsınız:

----------------- MENU --------------------

1- Rezervasyon  
2- Bütün Yolcuları Görüntüle  
3- Bütün Koltukları Görüntüle  
4- Bütün Boş Koltukları Görüntüle  
5- Çıkış

Her işlem sonrası menüye dönülür. Sistem kullanıcı hatalarına karşı dayanıklıdır ve yanlış girişlerde açıklayıcı uyarılar verir.

##  🔧 Gereksinimler
-  Python 3.x

##  📝 Notlar
-  Koltuk indeksleri 0'dan başladığı için kullanıcıdan alınan koltuk numarası int(koltukNO) - 1 olarak işlenir.

-  Kod, kullanıcı deneyimini artırmak için time.sleep() ile bekleme animasyonu içerir.

