from django.db import models

# Create your models here.
class Donor(models.Model):
    name = models.CharField(max_length=100,blank=True)
    email = models.EmailField(maxlength=254)
    image= models.ImageField(blank=True, upload_to='photos')
    contact = models.CharField(max_length=255)
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