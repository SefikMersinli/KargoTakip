from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home, name="anasayfa"),
    path('kargolar/', views.kargo_listesi, name="kargo_listesi"),
    path('kargolar/detay/', views.kargo_detay, name="kargo_detay"),
    path('kargolar/ekle/', views.kargo_ekle, name="kargo_ekle"), 
]