from django.db import models

# Create your models here.
from django.db import models

class Kargo(models.Model):
    
    takip_no = models.CharField(max_length=15, unique=True, verbose_name="Takip Numarası")
    
    # Alıcı Bilgileri
    alici_isim = models.CharField(max_length=100, verbose_name="Alıcı Adı Soyadı")
    alici_adres = models.TextField(verbose_name="Teslimat Adresi")
    
    # Kargo Durumu Seçenekleri (Seçimli Alan)
    DURUM_SECENEKLERI = [
        ('HAZIRLANIYOR', 'Sipariş Hazırlanıyor'),
        ('YOLDA', 'Kargo Yolda (Transfer Merkezi)'),
        ('DAGITIMDA', 'Dağıtıma Çıktı'),
        ('TESLIM', 'Teslim Edildi'),
        ('IPTAL', 'İptal Edildi'),
    ]
    durum = models.CharField(
        max_length=15,
        choices=DURUM_SECENEKLERI,
        default='HAZIRLANIYOR',
        verbose_name="Kargo Durumu"
    )

    # Finansal Bilgiler
    fiyat = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Kargo Ücreti")
    
    # Otomatik Zaman Damgaları
    olusturma_tarihi = models.DateTimeField(auto_now_add=True)
    guncelleme_tarihi = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.takip_no} - {self.alici_isim}"

    class Meta:
        verbose_name = "Kargo Gönderisi"
        verbose_name_plural = "Kargo Gönderileri"