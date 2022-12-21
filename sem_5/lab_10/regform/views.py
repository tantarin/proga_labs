from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('regform page')


def about(request):
    return render(request, 'regform/about.html', {})