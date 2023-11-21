from django.urls import path, include

from . import views
from .views import index

app_name = 'analytics'
urlpatterns = [
    path("analytics/", views.AnalyticsView.as_view(), name="analytics")

]