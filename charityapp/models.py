from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.
class Donor(models.Model):
    name = models.CharField(max_length=100,blank=True)
    email = models.EmailField(maxlength=254)
    image= models.ImageField(blank=True, upload_to='photos')
    contact = models.CharField(max_length=255)\
    
    def __str__(self):
        return f'{self.name}'
    def save_donor(self):
        self.save()
    def delete_donor(self):
        self.delete()

    @classmethod
    def search_donors(cls,search_term):
        donors=cls.objects.filter(name__icontains=search_term)
        return donors
      
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    phonenumber = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'


    def save(self, **kwargs):
        super().save()

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
