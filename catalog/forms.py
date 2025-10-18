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