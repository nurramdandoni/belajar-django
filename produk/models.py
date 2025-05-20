from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.IntegerField(max_length=11)
    price = models.FloatField()

