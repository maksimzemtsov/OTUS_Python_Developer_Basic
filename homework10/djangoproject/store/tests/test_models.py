import pytest
from store.models import Product, Category
from decimal import Decimal
import os
import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'djangoproject.settings'  # Указываем путь до настроек
django.setup()


@pytest.fixture
def category():
    return Category.objects.create(name='Тестовая категория', description='Описание')


@pytest.mark.django_db
def test_create_product(category):
    product = Product.objects.create(
        name='Тестовый товар',
        description='Описание',
        price=Decimal('100.00'),
        category=category
    )
    assert product.id is not None
    assert product.name == 'Тестовый товар'


@pytest.mark.django_db
def test_read_product(category):
    product = Product.objects.create(
        name='Продукт для чтения',
        description='Описание',
        price=Decimal('150.00'),
        category=category
    )
    retrieved = Product.objects.get(pk=product.pk)
    assert retrieved.name == 'Продукт для чтения'


@pytest.mark.django_db
def test_update_product(category):
    product = Product.objects.create(
        name='Обновляемый товар',
        description='Описание',
        price=Decimal('200.00'),
        category=category
    )
    product.name = 'Обновлённое имя'
    product.save()
    updated = Product.objects.get(pk=product.pk)
    assert updated.name == 'Обновлённое имя'


@pytest.mark.django_db
def test_delete_product(category):
    product = Product.objects.create(
        name='Удаляемый товар',
        description='Описание',
        price=Decimal('250.00'),
        category=category
    )
    product_id = product.pk
    product.delete()
    assert not Product.objects.filter(pk=product_id).exists()
