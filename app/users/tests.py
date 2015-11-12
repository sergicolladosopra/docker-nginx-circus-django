from django.test import TestCase
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase, force_authenticate, APIRequestFactory, APIClient
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django_dynamic_fixture import G, get
from django.contrib.auth.hashers import make_password
import json, uuid

class UserTests(APITestCase):
    user = None
    token = None
    password = 'apassword'

    @classmethod
    def setUpClass(self):
        super(UserTests, self).setUpClass()
        self.user = G(User, username=str(uuid.uuid1()), password=make_password(self.password), is_staff=1)
        self.token = Token.objects.get(user__username=self.user.username)

    def test_authentication_is_enabled(self):
        urls = ['/users/', '/groups/']
        for url in urls:
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authentication_returns_token_if_user_and_password_ok(self):
        url = '/api-token-auth/'
        response = self.client.post(url, {"username": self.user.username, "password": self.password}, 'json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('token' in response.data)
        self.assertIsNotNone(response.data['token'])


    def test_get_all_users(self):
        url = '/users/'
        self.client.credentials(HTTP_AUTHORIZATION='Token '+str(self.token))
        response = self.client.get(url)
        json_response = response.content.decode('ascii')

        self.assertTrue(self.user.username in json_response)
        self.assertTrue(self.user.email in json_response)
        self.assertTrue('count' in json_response)
