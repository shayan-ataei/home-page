from django.shortcuts import render
from django.http import HttpResponse



def product_index(req):
    template="product_index.html"
    return render(req, template)


def get_product(req):
    template="get_product.html"
    return render(req, template)


def list_product(req):
    template="list_product.html"
    return render(req, template)