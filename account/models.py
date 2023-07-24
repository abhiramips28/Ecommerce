from django.contrib.auth.models import UserManager, AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    username = models.CharField(unique=True,blank=True,null=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50,blank=True)
    last_name = models.CharField(max_length=50,blank=True)
    is_active = models.BooleanField()
    is_staff = models.BooleanField()
    is_superuser = models.BooleanField()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    objects = UserManager()

    def __str__(self):
        return self.email