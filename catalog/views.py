# from django.http import HttpResponse
# from django.shortcuts import render
from .models import Product
from django.views.generic import DetailView, DeleteView, ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy


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
    fields = ['name', 'image', 'description', 'price_per_item', 'category']
    template_name = 'catalog/create_form.html'
    success_url = reverse_lazy('product_list')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'image', 'description', 'price_per_item', 'category']
    template_name = 'catalog/create_form.html'
    success_url = reverse_lazy('product_list')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'catalog/delete_form.html'
    success_url = reverse_lazy('product_list')




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