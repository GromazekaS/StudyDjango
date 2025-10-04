from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# Create your views here.
def catalog_view(request):
    return render(request, 'catalog/base.html')


def contacts_view(request):
    return render(request, 'catalog/contacts.html')


def send_callback(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        print(f'Пользователь {name} оставил сообщение: {message}')
        return HttpResponse(f'Спасибо, {name}! Ваше сообщение получено')
    return render(request, 'catalog/contacts.html')


def product_list_view(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'catalog/product_list.html', context)


def product_details(request, pk):
    product = Product.objects.get(id=pk)
    context = {'product': product}
    return render(request, 'catalog/detailed_info.html', context)