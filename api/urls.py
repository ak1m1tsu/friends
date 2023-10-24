"""api endpoints"""
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView

urlpatterns = [
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("docs/", SpectacularRedocView.as_view(url_name="schema"), name="docs"),
    path("users/", include("users.urls")),
    path("auth/", include("auth.urls")),
    path("me/", include("me.urls")),
]
