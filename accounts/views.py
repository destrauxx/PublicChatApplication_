from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
# Create your views here.
from .forms import LoginForm, RegisterForm
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required

def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = User.objects.create_user(username, email, password, is_staff=False)
        user.save()
        user_profile = UserProfile(profile=user)
        user_profile.save()
        return redirect('/')
    return render(request, 'accounts/registration_form.html', {'form': form})

def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/')
        else:
            return redirect('/login/')
    return render(request, 'accounts/login_form.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/login/')
def profile_view(request):
    user = request.user
    return render(request, 'accounts/profile.html', {'profile': user})
    