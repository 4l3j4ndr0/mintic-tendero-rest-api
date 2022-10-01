from django.db import models
from .UserBussiness import Bussiness
from .Provider import Provider


class Product(models.Model):
    bussiness = models.ForeignKey(Bussiness, on_delete=models.CASCADE)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    product = models.CharField(max_length=255)
    description = models.CharField(max_length=500, null=True)
    bar_code = models.CharField(max_length=25)
    buy_price = models.DecimalField(max_digits=10, decimal_places=2)
    sell_price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    apply_iva = models.BooleanField(default=True)
    send_alert = models.IntegerField()

    class Meta:
        db_table = "products"
