"""users app serializers"""
from rest_framework import serializers

from .models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for User model
    """

    url = serializers.HyperlinkedIdentityField(
        view_name="user",
        lookup_field="username",
    )
    date_created = serializers.DateTimeField(read_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "username",
            "first_name",
            "last_name",
            "date_created",
            "url",
        )
