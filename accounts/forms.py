from re import M
from django.contrib.auth.forms import UserChangeForm , UserCreationForm
from django.contrib.auth import get_user_model



class CustomUserCreationForm(UserChangeForm):
    class Meta:
        
        model = get_user_model
        fields = ('email', 'username',)


class CustomUserChangeForm(UserCreationForm):

    class Meta:

        model = get_user_model
        fields = ('email','username',)