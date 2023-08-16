from django.db import models
from django.contrib.auth.models import User
from main.models import Tag

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    interests = models.ManyToManyField(Tag, blank=True)
    gender = models.CharField(max_length=200, blank=True, null=True, default="None")
    

    def __str__(self):
        return str(self.username)

#Not used
class Interest(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name