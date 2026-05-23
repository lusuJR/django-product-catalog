from django.shortcuts import render, get_object_or_404
from .models import Product

def product_list(request):
    products = Product.objects.all()

    search_query = request.GET.get('search')
    category_filter = request.GET.get('category')
    sort_price = request.GET.get('sort')

    if search_query:
        products = products.filter(name__icontains=search_query)

    if category_filter:
        products = products.filter(category__iexact=category_filter)

    if sort_price == 'low':
        products = products.order_by('price')
    elif sort_price == 'high':
        products = products.order_by('-price')
    else:
        products = products.order_by('-created_at')

    categories = Product.objects.values_list('category', flat=True).distinct()

    context = {
        'products': products,
        'categories': categories,
        'search_query': search_query,
        'category_filter': category_filter,
        'sort_price': sort_price,
    }

    return render(request, 'products/index.html', context)

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/detail.html', {'product': product})