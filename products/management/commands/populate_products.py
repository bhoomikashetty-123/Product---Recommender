from django.core.management.base import BaseCommand
from products.models import Product
import random

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        for i in range(50):
            Product.objects.create(
                name=f"Product {i}",
                category=random.choice(["Electronics", "Clothing", "Books"]),
                price=random.uniform(10, 500),
                description=f"Description for product {i}"
            )
