from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect
from .models import Product
from django.views.generic import View, DetailView, DeleteView, ListView, FormView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from .forms import CategoryForm, ProductForm, ContactForm
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .mixins import OwnerRequiredMixin, OwnerOrModeratorRequiredMixin
from django.contrib import messages
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator



class ProductListView(ListView):
    model = Product
    template_name = 'catalog/products_list.html'
    context_object_name = 'products'


@method_decorator(cache_page(60 * 15), name='dispatch')
class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/detailed_info.html'
    context_object_name = 'product'


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/create_form.html'
    success_url = reverse_lazy('products_list')

    def form_valid(self, form):
        # Автоматически назначаем текущего пользователя владельцем
        form.instance.owner = self.request.user
        return super().form_valid(form)

class ProductUpdateView(LoginRequiredMixin, OwnerRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/create_form.html'
    success_url = reverse_lazy('catalog:products_list')

    def get_form_class(self):
        # Возвращаем форму с передачей пользователя
        return ProductForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user  # Передаем пользователя в форму
        return kwargs

    def form_valid(self, form):
        if 'published' in form.cleaned_data:
            if not self.request.user.has_perm('catalog.can_publish_product'):
                form.add_error('published', 'У вас нет прав для публикации товаров')
                return self.form_invalid(form)
        return super().form_valid(form)

class ProductDeleteView(LoginRequiredMixin, OwnerOrModeratorRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/delete_form.html'
    success_url = reverse_lazy('catalog:products_list')
    permission_required = 'can_delete_product'


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


class PublishProductView(LoginRequiredMixin, View):
    def get(self, request, pk):
        return HttpResponse(f"GET запрос работает! PK: {pk}")

    def post(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        print(f"User: {request.user}")
        print(f"User permissions: {request.user.get_all_permissions()}")
        if not request.user.has_perm('catalog.can_unpublish_product'):
            print("User doesn't have the permission")
            return HttpResponseForbidden("У вас нет прав для снятия товара.")
        else:
            print("User has the permission")

        if not request.user.has_perm('catalog.can_unpublish_product'):
            return HttpResponseForbidden("У вас нет прав для снятия товара.")

        # Логика рецензирования книги
        product.published = request.POST.get('published')
        product.save()

        return redirect('catalog:product_detail', pk=pk)


# FBV views here.
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
# def products_list_view(request):
#     products = Product.objects.all()
#     context = {'products': products}
#     return render(request, 'catalog/products_list.html', context)
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