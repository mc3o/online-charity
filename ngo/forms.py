from django import forms
from .models import Donation
 
class DonationsForm(forms.ModelForm):

    class Meta:
        model = Donation
        fields=('name','description','category')

class RequestForm(forms.ModelForm):

    class Meta:
        model = Donation
        fields=('name','description','category')