from rest_framework import serializers
from subjects.models import Subjects, SubjectRegistration
from students.serializers import StudentSerilaizer


class SubjectSerilaizer(serializers.ModelSerializer):

    class Meta:    
        model = Subjects
        fields = '__all__'



class SubjectRegistrationSerializer(serializers.ModelSerializer):
    student = serializers.ReadOnlyField(source='student.id')
    subject = serializers.ReadOnlyField(source='subject.id')
    
    class Meta:    
        model = SubjectRegistration
        fields = ('subject', 'student', 'date_joined', 'is_major',)

