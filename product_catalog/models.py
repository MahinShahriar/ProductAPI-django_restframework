from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    CATEGORY_LIST = [
        ('t-shirt', 'T-SHIRT'),
        ('watch', 'WATCH'),
        ('electric', 'ELECTRIC'),
        ('automobile', 'AUTOMOBILE')
    ]

    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField(max_length=5000)
    catalogue = models.CharField(max_length=30, choices=CATEGORY_LIST)
    seller = models.ForeignKey(User, related_name='products', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
