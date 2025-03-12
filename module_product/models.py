from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=225)
    barcode = models.CharField(max_length=225, null=True, blank=True)
    price = models.PositiveBigIntegerField(default=0)
    stock = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
