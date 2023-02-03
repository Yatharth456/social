from django.db import models
from user.models import UserModel
# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='post')
    post = models.ImageField(upload_to="blog", height_field=None, width_field=None, max_length=100)
    text = models.CharField(max_length=512, null=True)


class Comment(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name="users")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)

class Reply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='comment')
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name="userid")
    text = models.CharField(max_length=512, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
