from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

def Register(req):
    if(req.method == 'POST'):
        username = req.POST.get('username')
        email = req.POST.get('email')
        password1 = req.POST.get('password1')
        password2 = req.POST.get('password2')
        if password1!=password2:
            return HttpResponse("Your password dosen't match.")
        else:
            new_user = User.objects.create_user(username,email,password1)
            new_user.save()
            return redirect('home')
    return render(req, 'app1/register.html')

def Login(req):
    if(req.method == 'POST'):
        username_f = req.POST.get('username')
        password_f = req.POST.get('password')
        user = authenticate(req, username = username_f, password = password_f)
        if user is not None:
            login(req, user)
            return redirect('home')
        else:
            return HttpResponse("In correct credentails")
    return render(req, 'app1/login.html')

def Logout(req):
    logout(req)
    return redirect('login')
