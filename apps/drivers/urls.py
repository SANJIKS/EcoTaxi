from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DriverLocationUpdateView


from django.urls import path

urlpatterns = [
    path('driver-location/<int:pk>/', DriverLocationUpdateView.as_view(), name='driver-location'),
]

