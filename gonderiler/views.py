from django.shortcuts import render, get_object_or_404
from.models import Kargo

# Create your views here.

def home(request):
    context = {}
    return render(request, 'home.html', context)



def kargo_listesi(request):

    gonderiler= Kargo.objects.all()

    is_admin= True

    context = {
        "baslik": "Kargo Takip Listesi",
        "gonderiler": gonderiler,
        "is_admin": is_admin,
    }
    
    
    return render(request, "kargo_listesi.html", context)



def kargo_detay(request, takip_no):

    detay = get_object_or_404(Kargo, takip_no=takip_no)
   

    context = { 
        "takip_no": takip_no,
        "detay": detay
    }
    return render(request, "kargo_detay.html", context)