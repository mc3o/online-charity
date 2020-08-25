from django.db import models

# Create your models here.
class Donor(models.Model):
    name = models.CharField(max_length=100,blank=True)
    email = models.EmailField(maxlength=254)
    image= models.ImageField(blank=True)
    contact = models.CharField(max_length=255)
    def __str__(self):
        return f'{self.name}'
    def save_donor(self):
        self.save()
    def delete_donor(self):
        self.delete()