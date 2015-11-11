from django.test import TestCase
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase, force_authenticate, APIRequestFactory
from rest_framework.authtoken import views
from django.contrib.auth.models import User
from django_dynamic_fixture import G, get
from django.contrib.auth.hashers import make_password
from .views import UserViewSet
import json, uuid

class UserTests(APITestCase):
    user = None
    password = 'apassword'

    @classmethod
    def setUpClass(self):
        super(UserTests, self).setUpClass()
        self.user = G(User, username=str(uuid.uuid1()), password=make_password(self.password))

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

    def test_get_all_users_forcing_authentication(self):
        url = '/users/'

        factory = APIRequestFactory()
        view = UserViewSet.as_view({'get': 'list'})

        request = factory.get(url)
        force_authenticate(request, user=self.user)
        response = view(request)
        #print(vars(response))



