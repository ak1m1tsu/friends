"""me app endpoints"""
from django.urls import path

from .views import Me

urlpatterns = [path("", Me.as_view(), name="me")]
