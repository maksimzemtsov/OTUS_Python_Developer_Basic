from django.contrib import admin
from .models import Product, Category
from decimal import Decimal


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "category")
    list_filter = ("category",)
    search_fields = ("name", "description")

    @admin.action(description="Уменьшить цену на 10%%")
    def discount_price(self, request, queryset):
        for product in queryset:
            product.price *= Decimal('0.9')
            product.save()
        self.message_user(request, f"Цены снижены на 10%!")

    actions = [discount_price]
