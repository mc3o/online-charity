from django import forms
# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, User, Donor, NGO
from crispy_forms.helper import FormHelper
from django.db import transaction


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    firstname = forms.CharField(max_length=100)
    lastname = forms.CharField(max_length=100)
    class Meta:
        model = User
        fields = ('username','firstname', 'lastname', 'email', 'password1', 'password2')


class NgoSignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    username = forms.CharField(max_length=100)
    location = forms.CharField(max_length=100)
    url = forms.URLField()
    phonenumber = forms.CharField()
    image = forms.ImageField()

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'username', 'location', 'url', 'phonenumber', 'image', 'password1', 'password2')

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_ngo = True
        
        user.save()
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        location = self.cleaned_data.get('location')
        url = self.cleaned_data.get('url')
        phone = self.cleaned_data.get('phonenumber')
        image = self.cleaned_data.get('image')

        print(image)
        ngo = NGO.objects.create(
            user=user, 
            name=username,
            location= location,
            phone = phone,
            email = email,
            image = image,
            url = url
            )
        return user
class DonorSignupForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    firstname = forms.CharField(max_length=100)
    lastname = forms.CharField(max_length=100)
    phonenumber = forms.CharField()

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username','firstname', 'lastname', 'email', 'password1', 'password2', 'phonenumber')

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_donor = True
        # if commit:
        #     user.save()
        # print(username)
        user.save()
        email = self.cleaned_data.get('email')
        firstname = self.cleaned_data.get('firstname')
        lastname = self.cleaned_data.get('lastname')
        email = self.cleaned_data.get('email')
        phonenumber = self.cleaned_data.get('phonenumber')
        username = self.cleaned_data.get('username')

        print(username)
        donor = Donor.objects.create(
            user=user,
            name = username,
            email = email,
            contact = phonenumber
            )
        
        return user


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


class DonorUpdateForm(forms.ModelForm):    
    class Meta:
        model = Donor
        fields = ['name','email', 'image', 'contact']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)

class NgoUpdateForm(forms.ModelForm):

    class Meta:
        model = NGO
        fields = ['location', 'phone', 'email', 'image']

