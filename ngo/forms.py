from django import forms
from .models import Donations
 
class DonationsForm(forms.ModelForm):
    class Meta:
        model=Donations
        fields=('name','description','category','photo_image')
class RequestForm(forms.ModelForm):
    class Meta:
        model = Donations
        fields=('name','description','category','email')