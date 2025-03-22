from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages


def home_page(request):
    return render(request,"website/home.html")


def login_user(request):
    # check if the user is logged in ?
    if request.method == "POST" :

        data = request.POST
        print(data,"\n")

        username = data.get("username")
        password = data.get("password")
        print(username," ",password)

        # Authenticate
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            messages.success(request , "you have been logged in.")
            return redirect("/home/")

        else :
            messages.success(request , "Invalid User credentials.please try again")
            return redirect("/login/")

    return render(request,"website/login.html")



def logout_user(request):
    logout(request)
    messages.success(request,"you are logged out")
    return redirect("/home/")


def register_user(request) :
    if request.method == "POST" :
        pass

        return redirect()
    return render(request,"website/register.html")
