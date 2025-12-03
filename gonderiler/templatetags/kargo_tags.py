from django import template
# template.Library nesnesini oluşturarak, tag ve filtreleri kaydetmek için kullanıyoruz.
register = template.Library() 

# @register.simple_tag dekoratörünü kullanarak, bu fonksiyonu bir template tag'i olarak tanımlıyoruz.
@register.simple_tag
def kdv_ekle(fiyat, oran=20):
    """
    
    """
    try:
        fiyat = float(fiyat)
        oran = float(oran)
        kdvli_fiyat = fiyat + (fiyat * oran / 100)
        # Sadece iki ondalık basamak göstermek için formatlıyoruz
        return "{:.2f}".format(kdvli_fiyat)
    except:
        return fiyat # Hata durumunda orijinal fiyatı döndür