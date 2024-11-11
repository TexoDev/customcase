
from django.db import models
from django.contrib.auth.models import AbstractUser,Group,Permission

#Create your models here.
class Cases(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics')
    
class UserAccount(models.Model):
    nickname = models.CharField(max_length=40)
    username = models.CharField(max_length=40, unique=True)
    password = models.CharField(max_length=100)
    