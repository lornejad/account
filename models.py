from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=300, verbose_name='نام')
    last_name = models.CharField(max_length=300, verbose_name='نام خانوادگی',unique=True)
    username = models.CharField(max_length=300)
    medical_record = models.CharField(max_length=300,verbose_name='سابقه پزشکی')
    ECG = models.FileField(verbose_name='فایل نوار قلب')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    last_login = models.DateTimeField(default=timezone.now)
    date_joined = models.DateTimeField(default=timezone.now)
    USERNAME_FIELD = "last_name"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.last_name
