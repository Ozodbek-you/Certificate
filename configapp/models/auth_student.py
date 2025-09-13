from django.db import models
from .auth_user import *



class Student(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name