from django.urls import path 
from .views import *


urlpatterns = [
    path("home/",home_page,name="home_page"), 
    path("login/",login_user,name="login_user"),
    path("logout/",logout_user,name="logout_user"),
    path("register/",register_user,name="register_user"),
    path("record_user/<int:pk>",record_user,name="record_user"),
    path("delete_user/<int:pk>",delete_user,name="delete_user"),
    path("add_user/",add_user,name="add_user"),
]