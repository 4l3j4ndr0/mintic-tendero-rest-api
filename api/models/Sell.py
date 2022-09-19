from django.db import models
from .UserBussiness import Bussiness
from .Customer import Customer
from .Product import Product

class Sell(models.Model):
    bussiness = models.ForeignKey(Bussiness, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    discount_concept = models.CharField(max_length=500)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    
    class Meta:
        db_table = "sells"

class SellDetail(models.Model):
    sell = models.ForeignKey(Sell, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    iva = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        db_table = "sells_detail"