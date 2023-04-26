from django.http import HttpResponse
from django.shortcuts import render
from .models import User
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.shortcuts import redirect


def enter_enter(request):
    if request.POST:
        login = request.POST.get("login")
        password = request.POST.get("password")
        user = User.objects.filter(login=login)
        error = {"error": "Login or password is wrong!"}

        if user.exists():
            user = User.objects.filter(login=login, password=password)
            if user.exists():
                return HttpResponse(login + " добро пожаловать!")
            else:
                return render(request, "enter_enter.html", context=error)
        else:
            return render(request, "enter_enter.html", context=error)
    else:
        return render(request, "enter_enter.html")



def write_in_base(login,gmail,password):
    tom = User.objects.create(login=login, gmail=gmail, password=password)

def enter_register(request):
    if request.POST:
        login = request.POST.get("login")
        gmail = request.POST.get("gmail")
        password = request.POST.get("password")
        user = User.objects.filter(login=login)
        if User.objects.filter(login=login).exists() or User.objects.filter(gmail=gmail).exists():
            return HttpResponse("Пользователь уже существует!")
        else:
            write_in_base(login,gmail,password)
            return redirect('/')
    else:
        return render(request, "enter_register.html")