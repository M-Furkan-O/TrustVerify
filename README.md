TrustVerify - CLI Tool for File Integrity
TrustVerify, bir "Göndericinin" dosyaları imzalamasına ve bir "Alıcının" bu dosyaların hem bütünlüğünü (integrity) hem de kaynağını (origin) doğrulamasını sağlayan Python tabanlı bir komut satırı aracıdır. Proje, hashing (SHA-256) ve dijital imzaları (RSA) birleştirerek güvenli bir veri paylaşım altyapısı sunar.
+2

Özellikler

Hashing: Herhangi bir dosya (metin, PDF, resim) için SHA-256 hash değeri oluşturur.

Manifest Oluşturma: Bir dizini tarayarak dosya adlarını ve hash değerlerini içeren bir metadata.json dosyası oluşturur.

Dijital İmza (RSA): metadata.json dosyasını kullanıcının Özel Anahtarı (Private Key) ile imzalar.

Bütünlük Kontrolü: Dosyaların yetkisiz bir değişikliğe uğrayıp uğramadığını manifest üzerinden denetler.

Doğrulama: Göndericinin Açık Anahtarını (Public Key) kullanarak manifestin hem değişmediğini hem de gerçekten göndericiden geldiğini teyit eder.

Kullanılan Kütüphaneler

Projede aşağıdaki standart ve harici kütüphaneler kullanılmıştır:

hashlib: SHA-256 hashing işlemleri için.

cryptography: RSA anahtar çifti üretimi ve dijital imzalama işlemleri için.

Kullanım

Programı çalıştırmak için aşağıdaki komutları kullanabilirsiniz:

Anahtar Çifti Oluşturma:
python3 main.py --genkeys

Manifest Oluşturma (İmzalama Dahil):
python3 main.py --init test_folder

Bütünlük ve İmza Kontrolü:
python3 main.py --check

Proje Raporu Özeti

Neden sadece hash yeterli değildir?
Hash tek başına verinin değişip değişmediğini (Integrity) kanıtlar ancak veriyi kimin gönderdiğini (Identity) kanıtlayamaz. Bir saldırgan dosyayı değiştirip yeni bir hash oluşturabilir; bu yüzden kimlik doğrulaması için dijital imza gereklidir.

RSA ve İnkar Edilemezlik (Non-repudiation):
Özel anahtar (Private Key) sadece sahibinde bulunduğu için, bu anahtarla atılan bir imza verinin kesinlikle o kişiden geldiğini kanıtlar. Bu durum, göndericinin veriyi gönderdiğini inkar etmesini engeller.

Demo Videosu

Projenin çalışma mantığını ve test adımlarını içeren YouTube videosuna aşağıdaki linkten ulaşabilirsiniz:

Video Linki: [BURAYA YOUTUBE LİNKİNİ YAPIŞTIR] 

NOT: Bu README dosyası projenin bir parçası olarak hazırlanmıştır. Proje teslim tarihi 29/03/2026'dır.
