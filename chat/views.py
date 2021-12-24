from django import http
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.models import User
# Create your views here.
from .forms import ChatForm
from .models import ChatModel

# @login_required(login_url='/login/')
def index_view(request):
    form = ChatForm(request.POST or None)
    messages = ChatModel.objects.all()
    # if form.is_valid():
    #     obj = form.save(commit=False)
    #     obj.save()
    #     return redirect('index')
    return render(request, 'index.html', {'form': form, 'messages': messages})


@login_required(login_url='/login/')
def send_view(request):
    if request.method == 'POST':
        form = ChatForm(request.POST or None)
        if form.is_valid():
            text = form.cleaned_data.get('text')
            obj = ChatModel(user=request.user, text=text)
            obj.save()
    return HttpResponseRedirect(reverse('index'))