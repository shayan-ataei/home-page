from django.shortcuts import render
from django.http import HttpResponse



def home(req):
    template="home.html"
    return render(req, template)


def contact_us(req):
    template="contact_us.html"
    return render(req, template)



def account_index(req):
    template="account_index.html"
    return render(req, template)


def login(req):
    template="login.html"
    return render(req, template)


def logout(req):
    template="logout.html"
    return render(req, template)
    

# def getuser(req, id_user=None):
#     return HttpResponse("getuser" + str(id_user))


# def getuser_by_username(req, username=None):
#     return HttpResponse("getuser" + username)

