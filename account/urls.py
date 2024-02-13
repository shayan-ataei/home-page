from django.urls import path
from . import views


app_name='account'



urlpatterns = [
    path('', views.account_index, name='account_index'),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    # path("getuser/<int:id_user>", views.getuser, name="getuser"),
    # path("getuser/<str:username>", views.getuser_by_username, name="getuser_by_username"),
    # path('home/', views.account_index, name='account_index'),
]
