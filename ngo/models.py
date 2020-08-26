from django.db import models
import datetime as dt

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


