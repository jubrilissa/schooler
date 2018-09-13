from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from utils.constants import TEACHER



class Teacher(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.user_type == TEACHER:
        Teacher.objects.create(user=instance)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == TEACHER:
        instance.teacher.save()
