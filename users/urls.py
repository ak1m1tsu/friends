"""users app endpoints"""
from django.urls import path

from .views import ListUsers, RetrieveUser

urlpatterns = [
    path("", ListUsers.as_view(), name="users"),
    path("<str:username>/", RetrieveUser.as_view(), name="user"),
]
