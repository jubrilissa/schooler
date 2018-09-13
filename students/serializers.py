from rest_framework import serializers
from students.models import Student
from accounts.serializers import UserSerializer


class StudentSerilaizer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:    
        model = Student
        fields = '__all__'