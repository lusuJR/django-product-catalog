from django.shortcuts import render, get_object_or_404, redirect
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

def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)

    cart = request.session.get('cart', {})

    product_id = str(product.id)

    if product_id in cart:
        cart[product_id]['quantity'] += 1
    else:
        cart[product_id] = {
            'name': product.name,
            'price': float(product.price),
            'quantity': 1,
            'image': product.image.url if product.image else '',
        }

    request.session['cart'] = cart

    return redirect('cart_detail')


def cart_detail(request):
    cart = request.session.get('cart', {})

    total = 0
    for item in cart.values():
        item['subtotal'] = item['price'] * item['quantity']
        total += item['subtotal']

    return render(request, 'products/cart.html', {
        'cart': cart,
        'total': total
    })


def remove_from_cart(request, pk):
    cart = request.session.get('cart', {})

    product_id = str(pk)

    if product_id in cart:
        del cart[product_id]

    request.session['cart'] = cart

    return redirect('cart_detail')


def checkout(request):
    cart = request.session.get('cart', {})
    total = sum(item['price'] * item['quantity'] for item in cart.values())

    return render(request, 'products/checkout.html', {
        'cart': cart,
        'total': total
    })