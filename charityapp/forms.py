from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from crispy_forms.helper import FormHelper


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    firstname = forms.CharField(max_length=100)
    lastname = forms.CharField(max_length=100)
    class Meta:
        model = User
        fields = ('username','firstname', 'lastname', 'email', 'password1', 'password2')

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(max_length=150)


    class Meta:
        model = User
        fields = ['username','email']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)

class ProfileUpdateForm(forms.ModelForm):
    bio = forms.CharField()

    class Meta:
        model = Profile
        fields = ['image', 'bio', 'phonenumber']