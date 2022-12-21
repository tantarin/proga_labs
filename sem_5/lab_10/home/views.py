from django.http.response import HttpResponse
from django.shortcuts import render


def home_page_view(request):
    return render(request, 'home/main.html', {})
