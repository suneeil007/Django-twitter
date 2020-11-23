from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.
from .models import Product

User = get_user_model()

class ProductTestCase(TestCase):

    def setUp(self):
        user_a = User(username='cfe', email='cfe@gamil.com')
        user_a_pw = 'somepassword'
        self.user_a_pw = user_a_pw
        user_a.is_staff = True
        user_a.is_superuser = False
        user_a.save()
        user_a.set_password(user_a_pw)
        self.user_a = user_a
        user_b = User.objects.create_user('user_2', 'cfe2@gmail.com', 'somepassword')
        self.user_b = user_b
    
    def test_user_count(self):
        user_count = User.objects.all().count()
        self.assertEqual(user_count, 2)

    def test_invalid_request(self):
        self.client.login(username=self.user_b.username, password='somepassword')
        response = self.client.post('/products/create/', {'title': 'this is a valid test'})
        self.assertTrue(response.status_code, 200)    

    # def test_valid_request(self):
    #     self.client.login(username=self.user_a.username, password='somepassword')
    #     response = self.client.post('/products/create/', {'title': 'this is a valid test'})
    #     self.assertEqual(response.status_code, 200) 





