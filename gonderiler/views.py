from django.shortcuts import render

DUMMY_KARGOLAR = [
    {
        "takip_no": "ABC12345",
        "alici_isim": "Rumeysa Topal",
        "durum": "Dağıtıma Çıktı",
        "fiyat": "25.50 TL",
        "adres": "Büyükşehir Mahallesi, Gül Sokak No: 5",
        "tarih": "03.12.2025"
    },
    {
        "takip_no": "DEF67890",
        "alici_isim": "Mehmet Kuruoğlu",
        "durum": "Teslim Edildi",
        "fiyat": "40.00 TL",
        "adres": "Küçükköy Caddesi, Karanfil Apt. No: 12",
        "tarih": "01.12.2025"
    },
    {
        "takip_no": "GHI11223",
        "alici_isim": "Zeynep Çavuş",
        "durum": "Sipariş Hazırlanıyor",
        "fiyat": "15.00 TL",
        "adres": "Üniversite Kampüsü, Merkez Bina",
        "tarih": "04.12.2025"
    },
    {
        "takip_no": "JKL44556",
        "alici_isim": "Ahmet Demir",
        "durum": "Kargo Yolda (Transfer Merkezi)",
        "fiyat": "30.75 TL",
        "adres": "Sanayi Sitesi, Atatürk Bulvarı No: 20",
        "tarih": "02.12.2025"
    }
]

def home(request):
    return render(request, 'home.html')

def kargo_listesi(request):
    
    gonderiler = DUMMY_KARGOLAR 
    
    context = {
        "baslik": "Kargo Yönetici Listesi",
        "gonderiler": gonderiler, 
    }
    
    return render(request, "gonderiler/kargo_listesi.html", context) 

def kargo_detay(request):
    takip_no = request.GET.get('takip_no_input')
    detay_kargo = None

    if takip_no:
        for kargo in DUMMY_KARGOLAR:
            if kargo["takip_no"] == takip_no:
                detay_kargo = kargo
                break
    if detay_kargo is None:
        detay_kargo = {
            "takip_no": takip_no if takip_no else "Bilinmiyor",
            "alici_isim": "Kayıt Bulunamadı",
            "durum": "Hata: Geçersiz Takip Numarası",
            "fiyat": "---",
            "adres": "Aradığınız numaraya ait kayıt bulunamamıştır.",
            "tarih": "---"
        }

    context = { 
        "takip_no": detay_kargo["takip_no"],
        "detay": detay_kargo,
    }
    
    return render(request, "gonderiler/kargo_detay.html", context)

def kargo_ekle(request):
    
    if request.method == 'POST':
        pass 
    
    context = {
        "durumlar": [
            'Sipariş Hazırlanıyor',
            'Kargo Yolda (Transfer Merkezi)',
            'Dağıtıma Çıktı',
            'Teslim Edildi',
            'İptal Edildi',
        ]
    }
    return render(request, "gonderiler/kargo_ekle.html", context)