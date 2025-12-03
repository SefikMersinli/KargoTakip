from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required 

# Create your views here.

# ========================================================
# 1. GİRİŞ (LOGIN) İŞLEMİ - Düzeltilmiş ve Tamamlanmış
# ========================================================
def login_view(request):
    if request.method == "POST":
        
        
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Hoş geldiniz, {user.username}!") 
            
            
            return redirect("profile") 
        else:
           
            messages.warning(request, "Kanka kullanıcı adı ya da şifre yanlış gözlerini bir baktır kanka 😂") 
            return render(request, "login.html")
            
    # GET metoduyla gelindiyse (sayfayı ilk açma)
    return render(request, "login.html")



def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            messages.warning(request, "Girdiğin şifreler uyuşmuyor gözlerini bir baktır kanka 😂")
            return render(request, "register.html")
            
        if User.objects.filter(username=username).exists():
            messages.warning(request, "Kanka seçtiğin kullanıcı adı baya popüler sanırım başkası almış bile 😄")
            return render(request, "register.html")
            
        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email
        )
        user.save()
        login(request, user)
        messages.success(request, f"Kayıt başarılı! Giriş yapıldı.")
        
    
        return redirect("profile") 
        
    return render(request, "register.html")

# ========================================================
# 3. ÇIKIŞ (LOGOUT) İŞLEMİ
# ========================================================
def logout_view(request):
    logout(request) 
    messages.success(request, "Başarıyla çıkış yapıldı.")
    return redirect("anasayfa")

# ========================================================
# 4. PROFİL (DETAY) SAYFASI
# ========================================================
@login_required 
def user_profile(request):
    # Bu fonksiyon, profile.html şablonunu çağırır.
    return render(request, "profile.html")