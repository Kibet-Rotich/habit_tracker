from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """
    Custom User model extending Django's AbstractUser.
    Includes additional fields like profile_settings.
    """
    profile_settings = models.JSONField(
        null=True,
        blank=True,
        default=dict,
        help_text="User-specific settings stored as JSON. For example, {'theme': 'dark', 'notifications': true}."
    )

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',  # Avoid conflict with auth.User.groups
        blank=True,
        help_text="The groups this user belongs to."
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',  # Avoid conflict with auth.User.user_permissions
        blank=True,
        help_text="Specific permissions for this user."
    )

    def __str__(self):
        return self.username
