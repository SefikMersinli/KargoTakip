from django.contrib import admin
from .models import Kargo 

# 1. Kargo modelinin Admin görünümünü özelleştiren sınıf
class KargoAdmin(admin.ModelAdmin):
    # Listeleme sayfasında gösterilecek kolonlar
    list_display = ('takip_no', 'alici_isim', 'durum', 'fiyat', 'guncelleme_tarihi')
    
    # Filtreleme çubuğunda kullanılacak alanlar
    list_filter = ('durum', 'guncelleme_tarihi')
    
    # Arama kutucuğunda arama yapılacak alanlar
    search_fields = ('takip_no', 'alici_isim', 'alici_adres')
    
    # Detay sayfasındaki alanları gruplandırma (Ders notlarınızdaki fieldsets)
    fieldsets = (
        ("Kargo Temel Bilgileri", {
            'fields': ('takip_no', 'durum', 'fiyat')
        }),
        ("Alıcı Bilgileri", {
            'fields': ('alici_isim', 'alici_adres')
        }),
    )

# 2. Modeli, özelleştirilmiş KargoAdmin sınıfı ile kayıt etme
admin.site.register(Kargo, KargoAdmin)