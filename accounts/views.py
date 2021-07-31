from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as django_logout
from django.contrib.auth.models import User, auth

# Create your views here.
def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)   
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, 'inavalid credentials')
            return redirect('login')

    else:
        return render(request, 'login.html')


# user registration
def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken . Try another')
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email taken . Try another') 
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                messages.info(request,'User registered')
                return redirect('login')

        else:
            messages.info(request,'Password doesnt match')
            return redirect('register')    
        return redirect('/')
    
    else:
        return render(request,'register.html')


def logout(request):
    django_logout(request)
    messages.info(request,'Logged out')
    return redirect('/')