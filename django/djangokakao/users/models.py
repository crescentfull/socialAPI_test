import profile
from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class SocialApi(models.Model):
    name = models.TextField()
    
    class Meta:
        db_table = 'sociai_api'
class User(models.Model):
    profile_nickname = models.CharField(max_length=40)
    profile_image    = models.CharField(max_length=1000, null=True)
    email           = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'users'