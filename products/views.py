from django.shortcuts import render, get_object_or_404
from .models import Product

def product_list(request):
    products = Product.objects.all().order_by('-created_at')
    return render(request, 'products/index.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/detail.html', {'product': product})