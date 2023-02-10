from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse

# Create your tests here.
class PostTest(APITestCase):
    def test_create_account(self):
        self.client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc1OTQ1OTk0LCJpYXQiOjE2NzU5NDI2OTQsImp0aSI6IjQ4MmYxNTQ3ZGY3ZTQ0MjBhZmRjYmE0NGIxNzBiMzVlIiwidXNlcl9pZCI6Mn0.-sDTh0gbHyLokuMC5JbUhYeF5IqsCFIkBRX3p6U09g8 ')

        url = reverse('blog')
        data = {
            "user": 1,
            "post": "",
            "text": "happy"
            }
        response = self.client.post(url, data, format='json')
  
class CmmentTest(APITestCase):
    def test_create_account(self):
        self.client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc1OTQ1OTk0LCJpYXQiOjE2NzU5NDI2OTQsImp0aSI6IjQ4MmYxNTQ3ZGY3ZTQ0MjBhZmRjYmE0NGIxNzBiMzVlIiwidXNlcl9pZCI6Mn0.-sDTh0gbHyLokuMC5JbUhYeF5IqsCFIkBRX3p6U09g8 ')

        url = reverse('comment')
        data = {
            "user": 1,
            "post": 2,
            "body": "wowwww....."
            }
        response = self.client.post(url, data, format='json')


class ReplyTest(APITestCase):
    def test_create_account(self):
        self.client.credentials(HTTP_AUTHORIZATION='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc1OTQ1OTk0LCJpYXQiOjE2NzU5NDI2OTQsImp0aSI6IjQ4MmYxNTQ3ZGY3ZTQ0MjBhZmRjYmE0NGIxNzBiMzVlIiwidXNlcl9pZCI6Mn0.-sDTh0gbHyLokuMC5JbUhYeF5IqsCFIkBRX3p6U09g8 ')

        url = reverse('reply')
        data = {
            "comment": 1,
            "user": 2,
            "text": "thanks"
            }
        response =self.client.post(url, data, format='json')