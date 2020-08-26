from django.contrib.auth.models import User
from django.db import models
import datetime as dt

# from pyuploadcare.dj.models import ImageField
# from tinymce.models import HTMLField


# Create your models here.

class NGO(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=50,)
    location = models.CharField(max_length=50,)
    case = models.CharField(max_length=100,)
    phone = models.CharField(max_length=20, blank=False,)
    email = models.CharField(max_length=30,)
    image = models.ImageField(blank=True,)

    def create_ngo(self):
        self.save()

    def delete_ngo(self):
        self.delete()

    @classmethod
    def search_by_name(cls, id_):
        ngo = cls.objects.filter(name=id)

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
        
class Donations(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    photo_image = models.ImageField(upload_to = 'photos/')

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


