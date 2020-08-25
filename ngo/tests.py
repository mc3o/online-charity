from django.test import TestCase
from .models import NGO


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
