from django.shortcuts import render
from .models import ProductCategory, Product


def index(request):
    context = {
        'title': 'Market Place'
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'Market Place - Каталог',
        'categories': ProductCategory.objects.all(),
        'products': Product.objects.all(),
    }
    return render(request, 'products/products.html', context)


