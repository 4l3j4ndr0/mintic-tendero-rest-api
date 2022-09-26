from django.db import models
from django.contrib.auth.models import User


class Bussiness(models.Model):
    name = models.CharField(max_length=100, unique=True)
    nit = models.CharField(max_length=20, unique=True)
    address = models.CharField(max_length=100)

    class Meta:
        db_table = "bussiness"


class UserBussiness(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bussiness = models.ForeignKey(Bussiness, on_delete=models.CASCADE)

    class Meta:
        db_table = "user_bussiness"
