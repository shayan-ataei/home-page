from django.urls import path
from . import views


app_name='product'



urlpatterns = [
    # path('', views.index_product, name='home'),
    path("", views.product_index, name="product_index"),
    path("get_product/", views.get_product, name="get_product"),
    path("list_product/", views.list_product, name="list_product"),
]