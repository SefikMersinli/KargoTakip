from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home, name="anasayfa"),
    path('kargolar/', views.kargo_listesi, name="kargo_listesi"),
    path('kargolar/<str:takip_no>/', views.kargo_detay, name="kargo_detay"),
]