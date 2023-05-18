from django import forms
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
from authentication.models import User


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')
