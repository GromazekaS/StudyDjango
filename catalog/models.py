from django.db import models
# from django.db.models.fields import DecimalField


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
    image =models.ImageField(
        upload_to="products/icons",
        blank=True,
        null=True,
        verbose_name="Иконка",
        help_text="Загрузите изображение товара"
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price_per_item = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        return f'Товар {self.name} из категории {self.category}, цена за штуку: {self.price_per_item}'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ['name']

        permissions = [
            ('can_unpublish_product', 'Может снимать с публикации товар'),
            ('can_delete_product', 'Может удалять товар'),
            # Добавим еще одно для публикации
            ('can_publish_product', 'Может публиковать товар'),        ]