from django.test import TestCase
from .models import NGO
from .models import Donation, Category
import datetime as dt



class CategoryTest(TestCase):
    def setUp(self):
        '''new instance before test'''
        self.hunger = Category(name='hunger')

    def tearDown(self):
        Category.objects.all().delete()

    def test_Category_instance(self):
        self.assertTrue(isinstance(self.hunger, Category))

    def test_save_category(self):
        self.hunger.save_category()
        category = Category.objects.all()
        self.assertEqual(len(category), 1)

    def test_update_category(self):
        self.hunger.save_category()
        self.hunger.update_category(self.hunger.id,'poverty')
        update = Category.objects.get(name = "poverty")
        self.assertEqual(update.name, 'poverty')

    def test_delete_category(self):
        self.hunger.save_category()
        category = Category.objects.all()
        self.assertEqual(len(category),1)
        self.hunger.delete_category()
        categories2 = Category.objects.all()
        self.assertEqual(len(categories2),0)

class DonationTestClass(TestCase):
    def setUp(self):
    
        self.disaster = Category( name= "disaster")
        self.samaritan = Donation(name ='Cry for help', description = 'Donation towards those affected by the recent floods', category= self.disaster)

    def tearDown(self):
       
        Donation.objects.all().delete()
        Category.objects.all().delete()

    def test_donations_instance(self):
       
        self.assertTrue(isinstance(self.samaritan, Donation))
