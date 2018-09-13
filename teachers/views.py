from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from teachers.models import Teacher
from teachers.serializers import TeacherSerializer


class TeacherView(APIView):
    def get(self, request, format=None):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)


class TeacherDetailView(APIView):

    def put(self, request, teacher_id, format=None):

        teacher = get_object_or_404(Teacher, pk=teacher_id)
        serializer = TeacherSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, teacher_id, format=None):
        teacher = get_object_or_404(Teacher, pk=teacher_id)
        teacher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
