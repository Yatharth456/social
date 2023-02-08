from django.db import models
from user.models import UserModel
# Create your models here.
class UserFollowing(models.Model):
    user_id = models.ManyToManyField(UserModel, related_name="following")
    following_user_id = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name="followers")
    created = models.DateTimeField(auto_now_add=True)