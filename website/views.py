from django.shortcuts import render



def home_page(request):
    return render(request,"base.html")


def login_page(request):
    return render(request,"website/login.html")
