from django import forms
from .models import Donation, MadeDonation, Category
 
class DonationForm(forms.ModelForm):

    class Meta:
        model = MadeDonation
        fields= ['amount']

class RequestForm(forms.ModelForm):

    class Meta:
        model = Donation
        fields=('name','description','category')

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'