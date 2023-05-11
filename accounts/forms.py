from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import password_validation
from accounts.models import Account



class LoginForm(AuthenticationForm):

    email = forms.EmailField(widget=forms.TextInput(attrs={
        'class':'form-controll',
        'placeholder':'Email'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-controll',
        'placeholder':'Password'
    }))


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", 'class': 'form-control',
                'placeholder': 'Password'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", 'class': 'form-control',
                'placeholder': 'Confirm Password'}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )
    class Meta:
        model = Account
        fields = (
            'username',
            'email',
            'password1',
            'password2'
        )
        widgets = {
           
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }),
        }