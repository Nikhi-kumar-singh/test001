from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from .forms import SignUpForm
from .models import record


def home_page(request):
    rec = record.objects.all()
    # print(rec[0].first_name)
    # print(rec[0].last_name)
    # print(rec)
    return render(request,"website/home.html",{'record':rec})


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
         
        if form.is_valid():
            form.save()
            user_name = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            messages.success("success registered.")
            return redirect("/home/")
        
    else :
        form = SignUpForm()
        return render(request,"website/register.html",{'orm':form})



def record_user(request , pk):
    t_pk = pk - 1
    data_obj = record.objects.filter(id = pk)
    # print(data_obj)

    if data_obj is not None :
        # print(data_obj)
        return render(request,"website/record.html",{'data':data_obj[0]})



def delete_user(request , pk):
    record.objects.filter(id = pk).delete()
    rec = record.objects.all()
    return redirect("/home/")



def add_user(request):
    if request.method == "POST" :

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zipcode = request.POST.get('zipcode')


        new_record = record(
            first_name = first_name,
            last_name = last_name,
            email = email,
            phone = phone,
            address = address,
            city = city,
            state = state,
            zipcode = zipcode
        )
        new_record.save()
    return redirect("/home/")




#  created_at =   models.DateTimeField(auto_now_add=True)
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     email = models.CharField(max_length=50)
#     phone = models.CharField(max_length=12)
#     address = models.CharField(max_length=150)
#     city = models.CharField(max_length=50)
#     state = models.CharField(max_length=50)
#     zipcode = models.CharField(max_length=10)
     