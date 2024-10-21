from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from Clothes.utils import menu
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
path_temp = path4images = os.path.join(base_dir, '../Clothes/templates/logreg')

def login(request):
    context = {}
    context["menu"] = menu
    if request.method == "POST":
        username = request.POST.get("user_name")
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('../Brands')
        else:            
            context["error"] = "Incorrect username or password"
            render(request, f"{path_temp}/login.html", context=context)
    return render(request, f"{path_temp}/login.html", context=context)

def logout(request):
    auth.logout(request)
    return redirect('/')

def register(request):
    context = {}
    context["menu"] = menu
    if request.method == "POST":
        user_name = request.POST['user_name']
        #user_email = request.POST['email']
        user_password1 = request.POST['password1']
        user_password2 = request.POST['password2']
        if user_password1 == user_password2:
            ##[+] if User.objects.filter(email=user_email).exists(): [+] print(f"[-] Email is exists: {user_email}") return redirect("register")
            if User.objects.filter(username=user_name).exists():
                context["error"] = "This login already exists"
                render(request, f"{path_temp}/register.html", context=context)
            else:
                user = User.objects.create_user(username=user_name, password=user_password1) #[+] email=user_email,
                user.save()
                return redirect("login")
        else:
            context["error"] = "Incorrect password"
            render(request, f"{path_temp}/register.html", context=context)
    return render(request, f"{path_temp}/register.html", context=context)