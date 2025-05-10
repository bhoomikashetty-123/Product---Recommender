from django.db import models

from products.models import Product

class Order(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return f"Order {self.id} at {self.timestamp}"
