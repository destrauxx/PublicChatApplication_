from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .forms import RegisterForm
from django.contrib.auth.models import User
from .models import UserProfile

def register_view(request):
    form = RegisterForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = User.objects.create(username, email, password)
            user.save()
            user_profile = UserProfile(user)
            user_profile.save()
            return redirect('/')
    return render(request, 'accounts/registration_form.html', {'form': form})
