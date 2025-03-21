from django.urls import path 
from .views import login_page,home_page


urlpatterns = [
    path("",home_page),
    path("login/",login_page),
]