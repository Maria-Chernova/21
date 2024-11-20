from django.shortcuts import render, redirect

from django.shortcuts import render, redirect, get_object_or_404
from .models import Phone

def index(request):
    return redirect('catalog')

def show_catalog(request):
    # Получаем все телефоны из базы данных
    phones = Phone.objects.all()
    template = 'catalog.html'
    context = {
        'phones': phones  # Передаем список телефонов в контекст
    }
    return render(request, template, context)

def show_product(request, slug):
    # Получаем телефон по slug, если не найден, возвращаем 404
    phone = get_object_or_404(Phone, slug=slug)
    template = 'product.html'
    context = {
        'phone': phone  # Передаем объект телефона в контекст
    }
    return render(request, template, context)