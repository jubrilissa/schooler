
from django.shortcuts import get_object_or_404
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from students.models import Student
from subjects.models import SubjectRegistration, Subjects
from subjects.serializers import (SubjectRegistrationSerializer,
                                  SubjectSerilaizer)
from teachers.models import Teacher


class SubjectView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        subjects = Subjects.objects.all()
        serializer = SubjectSerilaizer(subjects, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SubjectSerilaizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SubjectDetail(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def put(self, request, subject_id, format=None):
        subject = get_object_or_404(Subjects, pk=subject_id)
        serializer = SubjectSerilaizer(subject, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, subject_id, format=None):
        subject = get_object_or_404(Subjects, pk=subject_id)

        subject.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SubjectRegistrationView(APIView):

    def post(self, request, subject_id, format=None):
        student = get_object_or_404(Student, pk=request.data.get('student'))
        subject = get_object_or_404(Subjects, pk=subject_id)

        serializer = SubjectRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(student=student, subject=subject)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SubjectRegistrationDetailView(APIView):

    def put(self, request, registration_id, format=None):
        registration = get_object_or_404(SubjectRegistration, pk=registration_id)
        serializer = SubjectRegistrationSerializer(registration, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, registration_id, format=None):
        registration = get_object_or_404(
            SubjectRegistration, pk=registration_id)
        registration.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
