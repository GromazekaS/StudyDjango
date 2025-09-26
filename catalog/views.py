from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def catalog_view(request):
    return render(request, 'catalog/home.html')


def contacts_view(request):
    return render(request, 'catalog/contacts.html')


def send_callback(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        print(f'Пользователь {name} оставил сообщение: {message}')
        return HttpResponse(f'Спасибо, {name}! Ваше сообщение получено')
    return render(request, 'catalog/contacts.html')