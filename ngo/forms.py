from django import forms
from .models import Donation, MadeDonation
 
class DonationForm(forms.ModelForm):

    class Meta:
        model = MadeDonation
        fields= ['amount']

class RequestForm(forms.ModelForm):

    class Meta:
        model = Donation
        fields=('name','description','category')