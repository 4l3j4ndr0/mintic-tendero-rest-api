from django.db import models
from django.contrib.auth.models import User

class Bussiness(models.Model):
   name = models.CharField(max_length=100)
   nit = models.CharField(max_length=20)
   address = models.CharField(max_length=100)

class UserBussiness(models.Model):
   user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
   bussiness = models.ForeignKey(Bussiness, on_delete=models.DO_NOTHING)