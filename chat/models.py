from django.db import models
from django.contrib.auth.models import User

from datetime import datetime,timedelta
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
    active = models.BooleanField(default=False)
    chatowner = models.ManyToManyRel( related_name='owner_name',to=User , field=User.email)
    participants = models.ForeignKey(User, related_name="user_of_chat", on_delete=models.CASCADE)
    start_time = models.DateTimeField(default=datetime.now)
    #
    # def addSecs(secs):
    #     tm = datetime.now()
    #     fulldate = tm + timedelta(seconds=secs)
    #     return fulldate.time()

    #end_time = models.DateTimeField(default=addSecs(3600))
    def __str__(self):
        return str(self.name)