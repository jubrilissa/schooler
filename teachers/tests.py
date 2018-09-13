from django.urls import reverse_lazy
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from accounts.models import User
from teachers.models import Teacher
from utils.constants import STUDENT, TEACHER


class TeacherTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()

        self.teacher_user = User.objects.create_user(
            password='johndoe1234', email='teacher@gmail.com', user_type='teacher')

    
    def test_teacher_gets_created_with_user_type_studetnt_creation(self):
        User.objects.create_user(
            password='johndoe1234', email='teachertest1@gmail.com', user_type='teacher')
        test_user = User.objects.get(email='teachertest1@gmail.com')
        teacher = Teacher.objects.get(user=test_user)
        self.assertEqual(teacher.user, test_user)