from django.urls import reverse
from rest_framework.test import APITestCase


class PostsApiTestCase(APITestCase):
    def test_get(self):
        url = reverse('post-list')
        print(url)
        response = self.client.get(url)
        print(response.data)
