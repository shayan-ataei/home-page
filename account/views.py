from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User


def home(req):
    template="home.html"
    return render(req, template)


def contact_us(req):
    template="contact_us.html"
    return render(req, template)


def account_index(req):
    template="account_index.html"
    return render(req, template)


def _login(req):
    if req.method == "POST":
        username = req.POST.get("username", False)
        password = req.POST.get("password", False)
        if False not in [username, password]:
            if req.user.is_authenticated:
                return redirect("/account")
            user = authenticate(req, username=username, password=password)
            if user:
                login(request=req, user=user)
                return redirect("/")
        return render(req, "login.html")
    else:
        if req.user.is_authenticated:
            return redirect("/account")
        template="login.html"
        return render(req, template)


def _logout(req):
    logout(req)
    # return redirect("/account/login")
    template="home.html"
    return render(req, template)


def register(req):
    if req.method == "POST":
        username = req.POST.get("username", False)
        password = req.POST.get("password", False)
        email = req.POST.get("email", False)
        if False not in [username, password, email]:
            user = User.objects.create_user(username, email, password)
            user.save()
        template="login.html"
        return render(req, template)
    else:
        template="register.html"
        return render(req, template)
    


def getuser(req):
    user = User.objects.all()
    template="get_user.html"
    return render(req, template, {"getUser": user})

# def getuser(req, id_user=None):
#     return HttpResponse("getuser" + str(id_user))


# def getuser_by_username(req, username=None):
#     return HttpResponse("getuser" + username)

