from django.urls import path
from . import views
from . import views


app_name='account'



urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.account_index, name='account_index'),
    path('cta/', views.contact_us, name="contact_us"),
    path('users/', views.getuser, name="get_user"),
    path("login/", views._login, name="login"),
    path('register', views.register, name="register"),
    path("logout/", views._logout, name="logout"),
    # path("getuser/<int:id_user>", views.getuser, name="getuser"),
    # path("getuser/<str:username>", views.getuser_by_username, name="getuser_by_username"),
    
]
