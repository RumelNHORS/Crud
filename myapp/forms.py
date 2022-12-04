from django import forms
from . models import User
from django.core import validators


class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['id', 'name', 'subject', 'email', 'password']

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'subject': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(render_value=True, attrs={'class':'form-control'}),
        }