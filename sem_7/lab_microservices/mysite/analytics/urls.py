from django.urls import path, include

from .views import index

app_name = 'analytics'
urlpatterns = [
    # ex: /polls/
    path("", index),
]