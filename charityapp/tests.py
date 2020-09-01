from django.test import TestCase
from .models import NGO, User, Donor, Profile

# Create your tests here.
class NGOTest(TestCase):
    def setUp(self):
        self.me = User(is_donor=False, is_ngo=False)
        self.help = NGO(user=self.me, name="saveus", email="test@test.com", location="Nairobi", case="help the children",  phone="0704189013", url="http://test.com")

    def test_instance(self):
        self.assertTrue(isinstance(self.help,NGO))
        self.assertTrue(isinstance(self.me,User))

    def tearDown(self):
        NGO.objects.all().delete()

class DonorTest(TestCase):
    def setUp(self):
        self.john = User(is_donor=False, is_ngo=False)
        self.assist = Donor(user=self.john, name="hunger", email="john@test.com", contact="03040223")

    def test_instance(self):
        self.assertTrue(isinstance(self.assist,Donor))
        self.assertTrue(isinstance(self.john,User))

    def tearDown(self):
        NGO.objects.all().delete()

class ProfileTest(TestCase):
    def setUp(self):
        self.mat = User(is_donor=False, is_ngo=False)
        self.prof = Profile(user=self.mat, bio="Live life", phonenumber="0732434433")

    def test_instance(self):
        self.assertTrue(isinstance(self.prof,Profile))
        self.assertTrue(isinstance(self.mat,User))

    def tearDown(self):
        NGO.objects.all().delete()
    