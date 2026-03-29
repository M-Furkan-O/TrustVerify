TrustVerify - CLI Tool for File Integrity
TrustVerify, bir "Göndericinin" dosyaları imzalamasına ve bir "Alıcının" bu dosyaların hem bütünlüğünü (integrity) hem de kaynağını (origin) doğrulamasını sağlayan Python tabanlı bir komut satırı aracıdır. Proje, hashing (SHA-256) ve dijital imzaları (RSA) birleştirerek güvenli bir veri paylaşım altyapısı sunar.

Özellikler

Hashing: Herhangi bir dosya çin SHA-256 hash değeri oluşturur.

Manifest Oluşturma: Bir dizini tarayarak dosya adlarını ve hash değerlerini içeren bir metadata.json dosyası oluşturur.

Dijital İmza (RSA): metadata.json dosyasını kullanıcının Özel Anahtarı (Private Key) ile imzalar.

Bütünlük Kontrolü: Dosyaların yetkisiz bir değişikliğe uğrayıp uğramadığını manifest üzerinden denetler.

Doğrulama: Göndericinin Açık Anahtarını (Public Key) kullanarak manifestin hem değişmediğini hem de gerçekten göndericiden geldiğini teyit eder.

Kullanılan Kütüphaneler

hashlib: SHA-256 hashing işlemleri için.

cryptography: RSA anahtar çifti üretimi ve dijital imzalama işlemleri için.


Demo Videosu

Projenin çalışma mantığını ve test adımlarını içeren YouTube videosuna aşağıdaki linkten ulaşabilirsiniz:

Video Linki: https://youtu.be/ZXej8-LIrLc

NOT: Bu README dosyası projenin bir parçası olarak hazırlanmıştır.
