from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """Custom user creation form based on custom user"""
    """with additional fields."""

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'status')


class CustomUserChangeForm(UserChangeForm):
    """Custom user change form based on custom user"""
    """with additional fields."""

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'status')
