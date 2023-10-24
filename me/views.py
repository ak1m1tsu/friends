"""me app views"""
from rest_framework import authentication, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from users.models import User
from users.serializers import UserSerializer


class Me(APIView):
    """
    Retrieve, update or delete the authenticated user's profile.
    """

    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = UserSerializer

    def get_object(self, username):
        """
        Return a user by username.
        """
        return User.objects.get(username=username)

    def get(self, request):
        """
        Return the authenticated user's profile.
        """
        resp = JWTAuthentication().authenticate(request)
        if resp is None:
            return Response(
                data={
                    "success": False,
                },
                status=status.HTTP_401_UNAUTHORIZED,
            )

        user = self.get_object(resp[0].username)
        if user is None:
            return Response(
                data={
                    "success": False,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = UserSerializer(context={"request": request}, instance=user)

        return Response(
            data={
                "success": True,
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )
