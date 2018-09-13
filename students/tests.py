from django.urls import reverse_lazy
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from accounts.models import User
from students.models import Student
from utils.constants import STUDENT, TEACHER


class StudentTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()

        self.student_user = User.objects.create_user(
            password='johndoe1234', email='student@gmail.com', user_type='student')

    
    def test_student_gets_created_with_user_type_studetnt_creation(self):
        User.objects.create_user(
            password='johndoe1234', email='studenttest1@gmail.com', user_type='student')
        test_user = User.objects.get(email='studenttest1@gmail.com')
        student = Student.objects.get(user=test_user)
        self.assertEqual(student.user, test_user)
        
