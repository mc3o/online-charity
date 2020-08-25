from django.contrib.auth.models import User
from django.db import models
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
