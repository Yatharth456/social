from django.db import models
from user.models import UserModel
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json
from social.settings import CHANNEL_LAYER
# Create your models here.

class Notification(models.Model):
    NOTIFICATION_TYPE = ((1, 'post'), (2, 'comment'), (3, 'reply'))

    sender = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='noti_from_user', blank=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='noti_to_user', blank=True)
    notification_type = models.SmallIntegerField(choices=NOTIFICATION_TYPE)
    date = models.DateTimeField(auto_now_add=True)
    is_seen = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        channel_layer = get_channel_layer()
        notification_obj = Notification.objects.filter(is_seen=False).count()
        data = {'count': notification_obj, 'current_notification': self.notification_type}

        async_to_sync(channel_layer.group_send)(
            'test_consumer_group',{
                'type': 'send_notification',
                'value': json.dumps(data)
            }
        )
        super(Notification, self).save(*args, **kwargs)