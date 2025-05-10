from django.core.management.base import BaseCommand
from products.models import Product
from orders.models import Order
import random

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        Order.objects.all().delete()
        products = list(Product.objects.all())
        for _ in range(30):
            order = Order.objects.create()
            order.products.set(random.sample(products, random.randint(1, 5)))
