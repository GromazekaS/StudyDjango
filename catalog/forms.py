from django import forms
from .models import Product, Category
from django.core.exceptions import ValidationError

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
        fields = ['name', 'description', 'image', 'category', 'price_per_item']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        # Настройка атрибутов виджета для поля 'first_name'
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Введите наименование товара'  # Текст подсказки внутри поля
        })

        # Настройка атрибутов виджета для поля 'last_name'
        self.fields['description'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Введите описание товара'  # Текст подсказки внутри поля
        })

        # Настройка атрибутов виджета для поля 'email'
        self.fields['image'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Выберите изображение товара'  # Текст подсказки внутри поля
        })

        # Настройка атрибутов виджета для поля 'enrollment_date'
        self.fields['category'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Выберите категорию товара',  # Текст подсказки внутри поля
        })

        # Настройка атрибутов виджета для поля 'enrollment_date'
        self.fields['price_per_item'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Укажите цену товара',  # Текст подсказки внутри поля
        })

    def clean_name(self):
        print('Чистое название')
        name = self.cleaned_data['name']
        for spam in SPAM_WORDS:
            if spam in name.lower():
                raise ValidationError(f"Название содержит запрещенное слово: '{spam}'")
        return name

    def clean_description(self):
        print('Чистое описание')
        description = self.cleaned_data['description']
        for spam in SPAM_WORDS:
            if spam in description.lower():
                raise ValidationError(f"Описание содержит запрещенное слово: '{spam}'")
        return description

    def clean_price_per_item(self):
        print('Чистая цена')
        price = self.cleaned_data['price_per_item']
        if price < 0:
            raise ValidationError(f"Цена не может быть отрицательной '{price}'")
        return price