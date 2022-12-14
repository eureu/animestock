from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):
    # , initial='Имя'
    username = forms.CharField(label='Имя') 
    email = forms.EmailField(label='Email', max_length=244)
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']