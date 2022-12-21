from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('Hello, world')


def about(request):
    return render(request, 'regform/about.html', {})