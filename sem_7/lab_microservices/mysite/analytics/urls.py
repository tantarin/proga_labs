from django.urls import path, include

from . import views

app_name = 'analytics'
urlpatterns = [
    # ex: /polls/
    path("", views.IndexView.as_view(), name="index"),
]