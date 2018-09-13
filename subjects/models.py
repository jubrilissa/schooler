from django.db import models
from students.models import Student
from teachers.models import Teacher

# Create your models here.

class Subjects(models.Model):
    title = models.CharField(max_length=50)
    code = models.CharField(max_length=50)
    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE)


class SubjectRegistration(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    is_major = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)


    def save(self, *args, **kwargs):
        if self.is_major:
            try:
                temp = SubjectRegistration.objects.get(is_major=True, student=self.student)
                if self != temp:
                    temp.is_major = False
                    temp.save()
                    SubjectRegistration.objects.filter(is_major=self.is_major, student=self.student, subject=self.subject).delete()
            except SubjectRegistration.DoesNotExist:
                pass
        super(SubjectRegistration, self).save(*args, **kwargs)

