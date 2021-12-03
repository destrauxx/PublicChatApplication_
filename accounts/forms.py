from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput())