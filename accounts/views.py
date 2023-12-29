from django.shortcuts import render, redirect

# Create your views here.
from main.forms import UserForm
from django.contrib.auth import authenticate,login
from django.http import HttpResponse

def userLogin(request):
    invalidlogin=False
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            if user.is_authenticated:
                return redirect('index')
            else:
                # Invalid email or password. Handle as you wish
                return render(request, 'accounts/not_found_404.html')
            # return render(request, 'dashboard/login.html')
    return render(request, 'accounts/login.html')