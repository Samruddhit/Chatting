from django.db import models
from django.contrib.auth.models import User

from datetime import datetime
# Create your models here.
class Chatroom(models.Model):
    name = models.CharField(max_length=40, blank=False)
    active = models.BooleanField(default=False)
    participants = models.ForeignKey(User, related_name="user_of_order", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)


class UserProfile(models.Model):
    STATUS_CHOICES = (
        ('T', 'True'),
        ('F', 'False'),
    )
    user = models.OneToOneField(User, related_name='user_profile', on_delete=models.CASCADE)
    terms_condition = models.CharField(choices=STATUS_CHOICES, max_length=1)
    activation_key = models.CharField(max_length=40, blank=True, null=True)
    key_expires = models.DateTimeField(default=datetime.now)
    is_alive = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.user.email
