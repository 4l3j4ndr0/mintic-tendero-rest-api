from django.db import models
from .UserBussiness import Bussiness


class Provider(models.Model):
    bussiness = models.ForeignKey(Bussiness, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    cellphone = models.CharField(max_length=15)

    class Meta:
        db_table = "providers"
