from django.db import models
from django.db.models import DecimalField


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование')
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Категория товаров {self.name}"

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['name']


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование')
    description = models.TextField(null=True, blank=True)
    image =models.ImageField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE())
    price_per_item = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Товар {self.name} из категории {self.category}, цена за штуку: {self.price_per_item}'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ['name']

