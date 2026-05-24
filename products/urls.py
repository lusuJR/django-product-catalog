from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('', views.product_list, name='product_list'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),

    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:pk>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/increase/<int:pk>/', views.increase_quantity, name='increase_quantity'),
    path('cart/decrease/<int:pk>/', views.decrease_quantity, name='decrease_quantity'),

    path('checkout/', views.checkout, name='checkout'),

    path('login/', auth_views.LoginView.as_view(
        template_name='registration/login.html'
    ), name='login'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('categories/', views.categories, name='categories'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('orders/', views.order_history, name='order_history'),
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('dashboard/products/', views.admin_products, name='admin_products'),
    path('dashboard/orders/', views.admin_orders, name='admin_orders'),
    path('dashboard/customers/', views.admin_customers, name='admin_customers'),
    path('dashboard/analytics/', views.admin_analytics, name='admin_analytics'),
    path('dashboard/settings/', views.admin_settings, name='admin_settings'),
    path('dashboard/products/add/', views.admin_add_product, name='admin_add_product'),
    path('dashboard/products/edit/<int:pk>/', views.admin_edit_product, name='admin_edit_product'),
    path('dashboard/products/delete/<int:pk>/', views.admin_delete_product, name='admin_delete_product'),
    path(
    'dashboard/orders/update/<int:order_id>/<str:status>/',
    views.update_order_status,
    name='update_order_status'
),
path(
    'dashboard/orders/<int:order_id>/',
    views.admin_order_detail,
    name='admin_order_detail'
),
path(
    'payment/',
    views.payment_page,
    name='payment_page'
),
path('place-order/', views.place_order, name='place_order'),
path(
    'payment-success/<int:order_id>/',
    views.payment_success,
    name='payment_success'
),
path(
    'invoice/<int:order_id>/',
    views.download_invoice,
    name='download_invoice'
),
path(
    'products/<int:product_id>/review/',
    views.add_review,
    name='add_review'
),
path('wishlist/', views.wishlist, name='wishlist'),
path('addresses/', views.addresses, name='addresses'),
path('change-password/', views.change_password, name='change_password'),
path('account-settings/', views.account_settings, name='account_settings'),
path(
    'wishlist/add/<int:product_id>/',
    views.add_to_wishlist,
    name='add_to_wishlist'
),

path(
    'wishlist/remove/<int:wishlist_id>/',
    views.remove_from_wishlist,
    name='remove_from_wishlist'
),
]