"""users app views"""
from rest_framework import authentication, permissions
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import User
from .serializers import UserSerializer


class ListUsers(ListAPIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """

    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]
    queryset = User.objects.all()


class RetrieveUser(RetrieveAPIView):
    """
    View to retrieve a user in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """

    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]
    queryset = User.objects.all()
