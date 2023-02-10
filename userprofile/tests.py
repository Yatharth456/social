from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

# Create your tests here.
class UserLoginTestCase(APITestCase):    

    def test_create_account(self):
        token = self.client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc1OTQ1OTk0LCJpYXQiOjE2NzU5NDI2OTQsImp0aSI6IjQ4MmYxNTQ3ZGY3ZTQ0MjBhZmRjYmE0NGIxNzBiMzVlIiwidXNlcl9pZCI6Mn0.-sDTh0gbHyLokuMC5JbUhYeF5IqsCFIkBRX3p6U09g8')

        url = reverse('profile')
        data = {
            "users": 1,
            "first_name": "harinarayana",
            "last_name": "kumar",
            "gender": "M",
            "address": "noida",
            "mobile_no": "7889554455",
            "image": ""
            }
        response = self.client.post(url, data, format='json')