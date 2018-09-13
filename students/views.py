from django.shortcuts import get_object_or_404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from students.models import Student
from students.serializers import StudentSerilaizer


class StudentView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def get(self, request, format=None):
        students = Student.objects.all()
        serializer = StudentSerilaizer(students, many=True)
        return Response(serializer.data)


class StudentDetailView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def put(self, request, student_id, format=None):
        student = get_object_or_404(Student, pk=student_id)
        serializer = StudentSerilaizer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, student_id, format=None):
        student = get_object_or_404(Student, pk=student_id)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
