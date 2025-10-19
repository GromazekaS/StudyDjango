from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
from django.views.generic import DetailView, DeleteView, ListView, FormView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from .forms import CategoryForm, ProductForm, ContactForm
from django.core.mail import send_mail


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/detailed_info.html'
    context_object_name = 'product'


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/create_form.html'
    success_url = reverse_lazy('product_list')

    # def form_valid(self, form):
    #     print("Форма валидна!")  # Проверяем, вызывается ли этот метод
    #     return super().form_valid(form)
    #
    # def form_invalid(self, form):
    #     print("Форма невалидна! Ошибки:", form.errors)  # Выводим ошибки в консоль
    #     return super().form_invalid(form)


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/create_form.html'
    success_url = reverse_lazy('product_list')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'catalog/delete_form.html'
    success_url = reverse_lazy('product_list')


class ContactsView(FormView):
    template_name = 'catalog/contacts.html'
    form_class = ContactForm
    success_url = reverse_lazy('contacts')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'phone': '+7 (915) 544-97-89',
            'email': 'kinst@inbox.ru',
            'address': 'г. Москва, ул. Примерная, д. 1',
            'work_hours': 'Пн-Пт: 9:00-18:00'
        })
        return context

    def form_valid(self, form):
        # Обработка данных формы (отправка email и т.д.)
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']

        # Отправка email (пример)
        send_mail(
            f'Сообщение от {name}',
            message,
            email,
            ['kinst@inbox.ru'],
            fail_silently=False,
        )
        return super().form_valid(form)
# Create your views here.
# def catalog_view(request):
#     return render(request, 'catalog/base.html')
#
#
# def contacts_view(request):
#     return render(request, 'catalog/contacts.html')
#
#
# def send_callback(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         message = request.POST.get('message')
#         print(f'Пользователь {name} оставил сообщение: {message}')
#         return HttpResponse(f'Спасибо, {name}! Ваше сообщение получено')
#     return render(request, 'catalog/contacts.html')
#
#
# def product_list_view(request):
#     products = Product.objects.all()
#     context = {'products': products}
#     return render(request, 'catalog/product_list.html', context)
#
#
# def product_details(request, pk):
#     product = Product.objects.get(id=pk)
#     context = {'product': product}
#     return render(request, 'catalog/detailed_info.html', context)
#
#
# def menu(request):
#     return render(request, 'catalog/menu_example.html')