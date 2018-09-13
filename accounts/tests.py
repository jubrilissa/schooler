from django.urls import reverse_lazy
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from accounts.models import User
from utils.constants import STUDENT, TEACHER


class AuthenticationTestCase(APITestCase):

    """Testcase for the Authentication related API endpoints.
    """

    def setUp(self):
        self.client = APIClient()

        self.student_user = User.objects.create_user(
            password='johndoe1234', email='student@gmail.com', user_type='student')

    def test_user_can_signup(self):
        form_data = {
            'password': 'test234ggh83',
            'email': 'andela@andela.com',
            "first_name": "Oshey",
            "last_name": "baddest",
            'user_type': STUDENT
        }
        url = reverse_lazy('auth_register')
        response = self.client.post(url, form_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_incomplete_signup_returns_bad_request(self):
        # Does not contain email address
        bad_form_data = {
            'password': 'test234ggh83',
            "first_name": "Oshey",
            "last_name": "baddest",
            'user_type': STUDENT
        }
        url = reverse_lazy('auth_register')
        response = self.client.post(url, bad_form_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_get_token(self):
        data = {'username': 'student@gmail.com', 'password': 'johndoe1234'}
        url = reverse_lazy('gettoken')
        response = self.client.post(url, data, format='json')

        token = response.data.get('token')

        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(token)

    def test_unregistered_user_login_forbidden(self):

        response = self.client.post(
            reverse_lazy('gettoken'),
            {'username': 'janedoe', 'password': 'tia', }
        )
        self.assertEqual(response.status_code, 400)
