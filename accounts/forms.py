"""Accounts forms"""

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password


class SignupForm(forms.Form):
    """User form"""
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    password_confirmation = forms.CharField(widget=forms.PasswordInput())

    def clean_username(self):
        username = self.cleaned_data.get('username')
        user_exists = User.objects.filter(username=username).exists()

        if user_exists:
            raise forms.ValidationError('El nombre de usuario ya existe.')

        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_exists = User.objects.filter(email=email).exists()

        if email_exists:
            raise forms.ValidationError('El correo ya existe.')

        return email

    
    def clean(self):
        data = super().clean()
        password = data.get('password')
        password_confirmation = data.get('password_confirmation')

        if not password or password != password_confirmation:
            raise forms.ValidationError('Las contraseñas no coinciden')

        validate_password(password)

        return data


    def save(self):
        data = self.cleaned_data
        data.pop('password_confirmation')
        return User.objects.create_user(**data)

