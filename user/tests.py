from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from .models import UserModel

# Create your tests here.

# def create_user(self):
#     self.client = APIClient()
#     self.user = UserModel(email='test@gmail.com',password="test@123")
#     self.user.set_password("test@123")
#     self.user.save()
#     self.token = UserModel.objects.create(user=self.user)


class AccountTests(APITestCase):
    def test_create_account(self):
        url = reverse('register')
        data = {
            "email": "harinarayana@gmail.com",
            "password": "harinarayana@123"
            }
        response = self.client.post(url, data, format='json')
        # self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # self.assertEqual(UserModel.objects.count(), 1)
        # self.assertEqual(UserModel.objects.get().email, 'harinarayana@gmail.com')
