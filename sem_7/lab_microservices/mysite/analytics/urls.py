from django.urls import path, include

from . import views
from .views import index, AnalyticsView

urlpatterns = [
    path('analytics/', AnalyticsView.as_view(), name='analytics'),
]