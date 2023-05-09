from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """Custom user creation form based on custom user"""

    class Meta:
        model = CustomUser
        fields = ('username', 'email', )


class CustomUserChangeForm(UserChangeForm):
    """Custom user change form based on custom user"""

    class Meta:
        model = CustomUser
        fields = ('username', 'email', )
