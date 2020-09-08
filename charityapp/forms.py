from django import forms
# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, User, Donor, NGO
from crispy_forms.helper import FormHelper
from django.db import transaction


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, label='Email', widget=forms.TextInput(attrs={'placeholder':'abc@xyz.com'}))
    firstname = forms.CharField(max_length=100, label='FirstName', widget=forms.TextInput(attrs={'placeholder':'firstname'}))
    lastname = forms.CharField(max_length=100, label='LastName', widget=forms.TextInput(attrs={'placeholder':'lastname'}))
    username = forms.CharField(max_length=100, label='Username', widget=forms.TextInput(attrs={'placeholder':'username'}))
    class Meta:
        model = User
        fields = ('username','firstname', 'lastname', 'email', 'password1', 'password2')


class NgoSignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, label='Email',widget=forms.TextInput(attrs={'placeholder':'abc@xyz.com'}))
    username = forms.CharField(max_length=100, label='Username',widget=forms.TextInput(attrs={'placeholder':'username'}))
    location = forms.CharField(max_length=100, label='Location',widget=forms.TextInput(attrs={'placeholder':'100 abc street'}))
    url = forms.URLField(initial='http://')
    phonenumber = forms.CharField( label='PhoneNumber',widget=forms.TextInput(attrs={'placeholder':'075358901'}))
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
    email = forms.EmailField(max_length=254, label='Email', widget=forms.TextInput(attrs={'placeholder':'abc@xyz.com'}))
    firstname = forms.CharField(max_length=100, label='FirstName', widget=forms.TextInput(attrs={'placeholder':'firstname'}))
    lastname = forms.CharField(max_length=100, label='LastName', widget=forms.TextInput(attrs={'placeholder':'lastname'}))
    username = forms.CharField(max_length=100, label='Username', widget=forms.TextInput(attrs={'placeholder':'username'}))
    phonenumber = forms.CharField(label='Phonenumber', widget=forms.TextInput(attrs={'placeholder':'phonenumber'}))

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

