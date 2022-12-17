from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):
    # , initial='Имя'
    username = forms.CharField(label='Имя') 
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Пароль')
    password2 = forms.CharField(label='Подтвердите пароль')
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']