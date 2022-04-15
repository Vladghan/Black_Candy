from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

CustomUser = get_user_model()


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label="Имя*", max_length=150, required=True, widget=forms.TextInput())
    last_name = forms.CharField(label="Фамилия*", max_length=150, required=True, widget=forms.TextInput())
    middle_name = forms.CharField(label="Отчество", max_length=150, required=False, widget=forms.TextInput())
    email = forms.CharField(label="Email*", max_length=254, required=True, widget=forms.EmailInput())

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'middle_name', 'email', 'password1', 'password2',)
