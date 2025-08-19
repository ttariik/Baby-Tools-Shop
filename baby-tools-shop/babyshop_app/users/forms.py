# User authentication forms with German localization
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class RegisterForm(UserCreationForm):
    """
    Custom registration form with German placeholders and improved styling.
    Extends Django's UserCreationForm to include additional fields.
    """
    first_name=forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Vorname'
    }))
    last_name=forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Nachname'
    }))
    username=forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Benutzername'
    }))
    email=forms.CharField(widget=forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder':'E-Mail-Adresse'
    }))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Passwort'
    }))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Passwort wiederholen'
    }))
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password1','password2']




class LoginForm(forms.Form):
    """
    Custom login form with German placeholders and validation.
    """
    username=forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Benutzername'
    }))
    password=forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Passwort'
    }))


