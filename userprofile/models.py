from django.db import models
from user.models import UserModel

# Create your models here.
class Profile(models.Model):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    users = models.ForeignKey(UserModel, related_name="user", on_delete=models.DO_NOTHING,)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER, default="M")
    address = models.CharField(max_length=255, blank=True)
    mobile_no = models.CharField(max_length=10, blank=False)
    image = models.ImageField(upload_to="profile", height_field=None, width_field=None, max_length=100)

    def __str__(self):  
        return str(self.first_name)