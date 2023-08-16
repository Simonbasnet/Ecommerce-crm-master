from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MessageModel(models.Model):
    desc = models.CharField(max_length=100, blank=True)
    type = models.CharField(max_length=25, blank=True)
    priority = models.CharField(max_length=25, default="LOW")
    chats = models.ManyToManyField('Chat', related_name='messages')
    by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class Chat(models.Model):
    messagemodel = models.ForeignKey(MessageModel, on_delete=models.CASCADE)
    message = models.CharField(max_length=300, blank=True)
    sentby = models.ForeignKey(User, on_delete=models.CASCADE)


class Announcement(models.Model):
    message = models.CharField(max_length=400, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True)


class GeneralTaskModel(models.Model):
    task = models.CharField(max_length=300)
    completed = models.BooleanField(default=False)

class PersonalTaskModel(models.Model):
    task = models.CharField(max_length=300)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
