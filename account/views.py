from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")  # Redirect to home page or dashboard
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('account:login')  # Redirect to login page

    else:
        return render(request, 'login.html')  # Render login template

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('account:register')  # Redirect to register page
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email taken')
                return redirect('account:register')  # Redirect to register page
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                print('User  created')
                return redirect('account:login')  # Redirect to login page
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('account:register')  # Redirect to register page
    else:
        return render(request, 'register.html')  # Render register template

def logout(request):
    auth.logout(request)
    return redirect('/')  # Redirect to home page or login page