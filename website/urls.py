from django.urls import path 
from .views import *


urlpatterns = [
    path("home/",home_page,name="home_page"), 
    path("login/",login_user,name="login_user"),
    path("logout/",logout_user,name="logout_user"),
    path("register/",register_user,name="register_user"),
]