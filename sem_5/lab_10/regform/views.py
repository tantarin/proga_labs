from django.contrib import messages
from django.contrib.auth import login
from django.http import HttpResponse
from django.shortcuts import redirect, render

from regform.forms import RegisterForm


def index(request):
    return HttpResponse('regform page')


def about(request):
    return render(request, 'regform/about.html', {})


def signup(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'regform/register.html', {'form': form})

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You have singed up successfully.')
            login(request, user)
            return redirect('posts')
        else:
            return render(request, 'regformed/register.html', {'form': form})
