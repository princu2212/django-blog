from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from .forms import LoginForm, SignupForm

# Create your views here.
def login_page(request):
    
    form = LoginForm()

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("web:index")

    return render(request, 'accounts/login.html', {'form':form})

def signup_page(request):
    form = SignupForm()

    if request.method == "POST":
        data = SignupForm(request.POST)
        if data.is_valid():
            data.save()
            return redirect('accounts:login')

    return render(request, 'accounts/signup.html', {'form':form})

def logout_page(request):
    logout(request)
    return redirect('web:index')