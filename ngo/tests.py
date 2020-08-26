from django.test import TestCase
from .models import NGO
from .models import Donations, Category
import datetime as dt


# Create your tests here.
class NGOTestCase(TestCase):
    def setUp(self):
        self.new_ngo = NGO(name="orphanblack", location='kenya', case='orphanage donations', phone='+2547123456789',
                           email='email@gmail.com')

    def tearDown(self):
        NGO.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_ngo, NGO))

    def test_save_ngo(self):
        self.new_ngo.create_ngo()
        ngo = NGO.objects.all()
        self.assertTrue(len(ngo) > 0)

    def test_delete_ngo(self):
        self.new_ngo.create_ngo()
        self.new_ngo.delete_ngo()
        ngo = NGO.objects.all()
        self.assertEqual(len(ngo), 0)


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
        self.samaritan = Donations(name ='Cry for help', description = 'Donation towards those affected by the recent floods', category= self.disaster, photo_image = "wreck.jpg")

    def tearDown(self):
       
        Donations.objects.all().delete()
        Category.objects.all().delete()

    def test_donations_instance(self):
       
        self.assertTrue(isinstance(self.samaritan, Donations))
