from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages,auth

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request,user)
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    return render(request, 'login.html')
def logout(request):
    auth.logout(request)
    return render('/')

def register(request):
    if request.method == 'POST': 
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "User already exists")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already Exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password,email=email)
                user.save()
                return redirect('login')
                
        else:
                messages.info(request, 'Password Mismatch')
                return redirect('register')
        return redirect('/')
    
    return render(request, 'register.html')
