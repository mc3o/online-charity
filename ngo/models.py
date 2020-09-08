# from django.contrib.auth.models import User
from django.db import models
import datetime as dt
from charityapp.models import NGO, User, Donor
from django.urls import reverse


# from pyuploadcare.dj.models import ImageField
# from tinymce.models import HTMLField


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    @classmethod
    def update_category(cls,id,name):
        cls.objects.filter(id = id).update(name = name)

    @classmethod
    def display_all_categories(cls):
        return cls.objects.all()
        
class Donation(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    ngo = models.ForeignKey(NGO, on_delete=models.CASCADE, null=True)
    status = models.BooleanField(default=False)
    target = models.CharField(null=True, default=0, max_length=100)


    def save_donations(self):
        self.save()

    def __str__(self):
        return self.name

    def delete_donations(self):
        self.delete()

    @classmethod
    def filter_by_category(cls,category):
        searched = Category.objects.get(name = category)
        result = Donations.objects.filter(category = searched.id)
        return result

    @classmethod
    def display_all_donations(cls):
        return cls.objects.all()

    def get_absolute_url(self):
        return reverse('donation-detail', kwargs={'pk':self.pk}) 

class MadeDonation(models.Model):
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE, null=True)
    donation = models.ForeignKey(Donation, on_delete=models.CASCADE)
    amount = models.CharField(max_length=100)
    ngo = models.ForeignKey(NGO, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.amount


