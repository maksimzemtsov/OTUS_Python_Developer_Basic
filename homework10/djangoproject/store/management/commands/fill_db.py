from django.core.management.base import BaseCommand
from store.models import Category, Product
import random


class Command(BaseCommand):
    help = "Fill database with test data"

    def handle(self, *args, **kwargs):
        categories = ['Electronics', 'Clothing', 'Books', 'Toys']
        for cat in categories:
            category, _ = Category.objects.get_or_create(name=cat, description=f"Category {cat}")

            for i in range(5):
                Product.objects.create(
                    name=f"Product {i} in {cat}",
                    description=f"Description for product {i}",
                    price=random.uniform(10, 500),
                    category=category
                )

        self.stdout.write(self.style.SUCCESS("Data base was filled!"))
