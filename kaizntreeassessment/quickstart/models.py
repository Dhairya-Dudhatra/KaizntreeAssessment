from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Item(models.Model):
    sku = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    tags = models.ManyToManyField(Tag)
    stock_status = models.CharField(max_length=50)
    available_stock = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.name
# Create your models here.
