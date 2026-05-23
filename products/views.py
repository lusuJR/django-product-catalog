from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Order, OrderItem

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

def increase_quantity(request, pk):
    cart = request.session.get('cart', {})
    product_id = str(pk)

    if product_id in cart:
        cart[product_id]['quantity'] += 1

    request.session['cart'] = cart
    return redirect('cart_detail')


def decrease_quantity(request, pk):
    cart = request.session.get('cart', {})
    product_id = str(pk)

    if product_id in cart:
        if cart[product_id]['quantity'] > 1:
            cart[product_id]['quantity'] -= 1
        else:
            del cart[product_id]

    request.session['cart'] = cart
    return redirect('cart_detail')

@login_required
def checkout(request):
   
    cart = request.session.get('cart', {})
    if not cart:
        return redirect('cart_detail')

    total = sum(
        item['price'] * item['quantity']
        for item in cart.values()
    )

    if request.method == 'POST':

        order = Order.objects.create(
            user=request.user,
            total=total
        )

        for product_id, item in cart.items():

            product = Product.objects.get(id=product_id)

            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=item['quantity'],
                price=item['price']
            )

        request.session['cart'] = {}

        return redirect('order_history')

    return render(request,
                 'products/checkout.html',
                 {
                     'cart': cart,
                     'total': total
                 })

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('product_list')
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {
        'form': form
    })

@login_required
def order_history(request):

    orders = Order.objects.filter(
        user=request.user
    ).order_by('-created_at')

    return render(request,
                 'products/orders.html',
                 {'orders': orders})
@login_required
def profile(request):
    return render(request, 'products/profile.html')

def categories(request):
    categories = Product.objects.values_list(
        'category',
        flat=True
    ).distinct()

    return render(request,
                  'products/categories.html',
                  {'categories': categories})


def about(request):
    return render(request, 'products/about.html')

def contact(request):
    return render(request, 'products/contact.html')