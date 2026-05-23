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
]