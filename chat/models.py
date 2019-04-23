from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta


# Create your models here.


class UserProfile(models.Model):
    STATUS_CHOICES = (
        ('T', 'True'),
        ('F', 'False'),
    )
    user = models.OneToOneField(User, related_name='user_profile', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email


class Chatroom(models.Model):
    name = models.CharField(max_length=40, blank=False)
    start_time = models.DateTimeField(default=datetime.now)

    # def addSecs(secs):
    #     tm = datetime.now()
    #     fulldate = tm + timedelta(seconds=secs)
    #     return fulldate.time()

    end_time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return str(self.name)


class Message(models.Model):
    created_at = models.DateTimeField(default=datetime.now)
    messages = models.CharField(max_length=1000)
    # user_id = models.ForeignKey(to=UserProfile, on_delete=models.CASCADE)
    chat_id = models.ForeignKey(Chatroom, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.messages)
        #return str(self.chat_id + self.user_id)
