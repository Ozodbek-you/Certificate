from django.db import models
from datetime import timezone

from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email kiritilishi shart")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser uchun is_staff=True bo‘lishi kerak")

        return self.create_user(email=email, password=password, **extra_fields)

class BaseModel(models.Model):
    created_ed = models.DateField(auto_now_add=True)
    updated_ed = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractBaseUser,PermissionsMixin):
    phone_regex = RegexValidator(
        regex=r'^\+9989\d{8}$',
        message="Telefon raqam +9989XXXXXXXX formatida bo‘lishi kerak"
    )

    phone_number = models.CharField(
        validators=[phone_regex], max_length=13, unique=False
    )
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

    # @property
    # def is_superuser(self):
    #     return self.is_admin
