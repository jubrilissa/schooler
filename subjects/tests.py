from django.urls import reverse_lazy
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from rest_framework.authtoken.models import Token

from accounts.models import User
from teachers.models import Teacher
from utils.constants import STUDENT, TEACHER


class SubjectTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.student_user = User.objects.create_user(
            password='johndoe1234', email='student@gmail.com', user_type='student')
        print(f'I am the student id {self.student_user.id}')
        data = {'username': 'student@gmail.com', 'password': 'johndoe1234'}

        response = self.client.post(
            reverse_lazy('gettoken'), data, format='json')

        self.token = response.data.get('token')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)

        self.teacher_user = User.objects.create_user(
            password='johndoe1234', email='teacher@gmail.com', user_type='teacher')

    def test_wont_create_subject_without_title(self):
        form_data = {
            'code': 'assessment101',
            'teacher': self.teacher_user.id
        }
        url = reverse_lazy('create_subject')
        response = self.client.post(url, form_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
