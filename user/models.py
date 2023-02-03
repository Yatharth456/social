from django.db import models
from django.utils import timezone
from .managers import CustomUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin  

# Create your models here.

class UserModel(AbstractBaseUser):
    username = None
    email = models.EmailField(('email_address'), unique=True, max_length = 200)  
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'  
    REQUIRED_FIELDS = []
    objects = CustomUserManager()


    def __str__(self):  
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def is_staff(self):
        "Is the user a member of staff?"
        return self.is_staff


    def has_module_perms(self, app_label):
        return True