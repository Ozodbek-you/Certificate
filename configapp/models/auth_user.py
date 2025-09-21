from django.db import models
from datetime import timezone

from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin


class CustomUserManager(BaseUserManager):
    def create_user(self,phone_number,password = None,**extra_fields):
        if not phone_number:
            raise ValueError("Phone_number kiritilishi shart")
        user = self.model(phone_number = phone_number,**extra_fields)
        user.set_password(password)
        user.save(using = self._db)
        return user
    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)      # 🔹 muhim
        extra_fields.setdefault("is_superuser", True)  # 🔹 muhim
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser uchun is_staff=True bo‘lishi kerak")

        return self.create_user(phone_number, password, **extra_fields)
class BaseModel(models.Model):
    created_ed = models.DateField(auto_now_add=True)
    updated_ed = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractBaseUser,PermissionsMixin):
    password = models.CharField()
    sms_kod = models.CharField(max_length=4,null=True,blank=True)
    email = models.EmailField(unique=True,null=True,blank=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_staff  = models.BooleanField(default=False)

    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    def __str__(self):
        return self.email

    @property
    def is_superuser(self):
        return self.is_admin
