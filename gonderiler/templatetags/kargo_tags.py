from django import template

register = template.Library() 

@register.simple_tag
def kdv_ekle(fiyat, oran=20):
    
    try:
        fiyat = float(fiyat)
        oran = float(oran)
        kdvli_fiyat = fiyat + (fiyat * oran / 100)
        # Sadece iki ondalık basamak göstermek için formatlıyoruz
        return "{:.2f}".format(kdvli_fiyat)
    except:
        return fiyat