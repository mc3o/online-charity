from django import forms
from .models import Donation, MadeDonation, Category
 
class DonationForm(forms.ModelForm):
    amount = forms.IntegerField(label='Amount',widget=forms.TextInput(attrs={'placeholder':'amount e.g 700'}))
    class Meta:
        model = MadeDonation
        fields= ['amount']

class RequestForm(forms.ModelForm):
    target = forms.IntegerField(label='Target',widget=forms.TextInput(attrs={'placeholder':'amount e.g 70000'}))
    name = forms.CharField(label='Title of the donation',widget=forms.TextInput(attrs={'placeholder':'title'}))
    description = forms.CharField(label='Description',widget=forms.Textarea(attrs={'placeholder':'Describe the nature of the donation you are requesting'}))
    class Meta:
        model = Donation
        fields=['name','description','category', 'target']

class CategoryForm(forms.ModelForm):
    name = forms.CharField(label='Name',widget=forms.TextInput(attrs={'placeholder':'category name'}))

    class Meta:
        model = Category
        fields = '__all__'