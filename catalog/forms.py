from django import forms
from .models import Product, Category
from django.core.exceptions import ValidationError
from django.template.defaultfilters import filesizeformat
import os

SPAM_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=100)
    email = forms.EmailField(label='Email')
    message = forms.CharField(label='Сообщение', widget=forms.Textarea)


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description',]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'price_per_item', 'published']
        labels = {
            'name': 'Название товара',
            'category': 'Категория товара',
            'description': 'Описание товара',
            'price_per_item': 'Цена товара',
            'image': 'Изображение товара',
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(ProductForm, self).__init__(*args, **kwargs)

        # Настройка атрибутов виджета для поля 'name'
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Введите наименование товара'  # Текст подсказки внутри поля
        })

        # Настройка атрибутов виджета для поля 'description'
        self.fields['description'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Введите описание товара'  # Текст подсказки внутри поля
        })

        # Настройка атрибутов виджета для поля 'email'
        self.fields['image'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Выберите изображение товара'  # Текст подсказки внутри поля
        })

        self.fields['category'].empty_label = "Выберите категорию товара"
        # Настройка атрибутов виджета для поля 'category'
        self.fields['category'].widget.attrs.update({
            'class': 'form-select',  # Добавление CSS-класса для стилизации поля
        })

        # Настройка атрибутов виджета для поля 'price_per_item'
        self.fields['price_per_item'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Укажите цену товара',  # Текст подсказки внутри поля
        })

        # Если пользователь не имеет прав на публикацию - делаем поле read-only
        if self.user and not self.user.has_perm('catalog.can_publish_product'):
            self.fields['published'].disabled = True
            self.fields['published'].help_text = 'У вас нет прав для изменения статуса публикации'

        # Вот так был бы описан виджет checkbox'а в форме:
        self.fields['published'].widget.attrs.update({
            'class': 'form-check-input',
            'role': 'switch',  # для переключателя
            'id': 'id_track'
        })

    def clean_name(self):
        # print('Чистое название')
        name = self.cleaned_data['name']
        for spam in SPAM_WORDS:
            if spam in name.lower():
                raise ValidationError(f"Название содержит запрещенное слово: '{spam}'")
        return name

    def clean_description(self):
        # print('Чистое описание')
        description = self.cleaned_data['description']
        for spam in SPAM_WORDS:
            if spam in description.lower():
                raise ValidationError(f"Описание содержит запрещенное слово: '{spam}'")
        return description

    def clean_image(self):
        # print('Чистое изображение')
        image = self.cleaned_data.get('image', False)

        # Если изображение не загружено - пропускаем валидацию
        if not image:
            return image

        # Проверка размера файла (5 МБ = 5 * 1024 * 1024 байт)
        max_size = 5 * 1024 * 1024
        # print(f'Размер файла: {image.size}')
        if image.size > max_size:
            raise ValidationError(
                f'Размер файла не должен превышать 5 МБ. Ваш файл: {filesizeformat(image.size)}'
            )

        # Проверка расширения файла
        valid_extensions = ['.jpg', '.jpeg', '.png']
        ext = os.path.splitext(image.name)[1].lower()
        if ext not in valid_extensions:
            raise ValidationError(
                f'Недопустимый формат файла. Разрешенные форматы: {", ".join(valid_extensions)}'
            )

        # Проверка MIME-типа (дополнительная проверка)
        valid_mime_types = ['image/jpeg', 'image/png']
        if hasattr(image, 'content_type') and image.content_type not in valid_mime_types:
            raise ValidationError('Недопустимый тип файла. Разрешены только изображения.')

        return image

    def clean_price_per_item(self):
        # print('Чистая цена')
        price = self.cleaned_data['price_per_item']
        if price < 0:
            raise ValidationError(f"Цена не может быть отрицательной '{price}'")
        return price