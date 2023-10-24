"""users app models"""
from django.contrib.auth.base_user import AbstractBaseUser
from django.core.mail import send_mail
from django.db import models
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


class User(AbstractBaseUser):
    """Custom user model."""

    email = models.EmailField(
        verbose_name=_("email address"),
        unique=True,
    )

    friends = models.ManyToManyField(
        to="self",
        verbose_name=_("friends"),
    )

    username = models.CharField(
        verbose_name=_("username"),
        max_length=100,
        unique=True,
    )
    first_name = models.CharField(
        verbose_name=_("first name"),
        max_length=100,
        blank=False,
        null=False,
    )
    last_name = models.CharField(
        verbose_name=_("last name"),
        max_length=100,
        blank=False,
        null=False,
    )

    is_active = models.BooleanField(
        verbose_name=_("is active"),
        default=False,
    )
    is_staff = models.BooleanField(
        verbose_name=_("is staff"),
        default=False,
    )
    is_superuser = models.BooleanField(
        verbose_name=_("is superuser"),
        default=False,
    )

    created_at = models.DateTimeField(
        verbose_name=_("created at"),
        default=now,
    )
    updated_at = models.DateTimeField(
        verbose_name=_("updated at"),
        default=now,
    )

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "first_name", "last_name"]

    objects = UserManager()

    def get_full_name(self):
        """Return the first name plus the last name, with a space in between.
        If the first and last name are the same, return just the first name.
        This is used in the admin interface to display the full name of the user.
        """
        full_name = f"{self.first_name} {self.last_name}"
        if full_name.strip() == self.first_name.strip():
            return self.first_name
        return full_name

    def get_short_name(self):
        """Return the first name."""
        if self.first_name.strip() == self.last_name.strip():
            return self.first_name
        return self.first_name.split(" ", maxsplit=1)[0]

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def __str__(self):
        return self.email
