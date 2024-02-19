from django.urls import path
from . import views


app_name='product'



urlpatterns = [
    # path('', views.index_product, name='home'),
    path("product", views.product_index, name="product_index"),
    path("product/get/", views.get_product, name="get_product"),
    path("product/list/", views.list_product, name="list_product"),
]