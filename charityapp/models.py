from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image


# Create your models here.
class User(AbstractUser):
    is_donor = models.BooleanField(default=False)
    is_ngo = models.BooleanField(default=False)


class Donor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=100,blank=True)
    email = models.EmailField()
    image= models.ImageField(blank=True, upload_to='photos', default='default.jpg')
    contact = models.CharField(max_length=255, default='78736')
    
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

class NGO(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=50,)
    location = models.CharField(max_length=50,)
    case = models.CharField(max_length=100,)
    phone = models.CharField(max_length=20, blank=False,)
    email = models.CharField(max_length=30,)
    image = models.ImageField(blank=True, upload_to='photos')
    url = models.URLField(null=True)

    def create_ngo(self):
        self.save()

    def delete_ngo(self):
        self.delete()

    @classmethod
    def search_by_name(cls, id_):
        ngo = cls.objects.filter(name=id)           


class DonorProfile(models.Model):
    user = models.OneToOneField(Donor, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Profile'


    def save(self, **kwargs):
        super().save()

class NgoProfile(models.Model):
    user = models.OneToOneField(NGO, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.user.username} Profile'


    def save(self, **kwargs):
        super().save()


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
