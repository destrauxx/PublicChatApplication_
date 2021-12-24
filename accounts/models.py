from django.db import models
from django.contrib.auth.models import User
from django.db.models import OneToOneField
from django.db.models.fields import CharField
# Create your models here.

class UserProfile(models.Model):
    profile = OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
