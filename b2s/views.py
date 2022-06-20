from django.shortcuts import render, redirect
from users.forms import UserRegisterForm
from products.models import *

def home(request):
    menus = Menu.objects.all()
    categories = Category.objects.all()
    products = Product.objects.all()[:4]
    bestsell = Product.objects.all().order_by('-count_sold')[:4] 
    recommended = Product.objects.all().order_by('-price')[:4] 
    nav_products = Product.objects.all()

    if request.user.is_authenticated:
        customer = request.user.profile
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_item
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_item': 0, 'shipping': False}
        cartItems = order['get_cart_item']

    context = {
        'menus':menus,
        'categories':categories,
        'products':products,
        'nav_products':nav_products,
        'bestsell':bestsell,
        'recommended':recommended,
        'items': items,
        'order': order,
        'cartItems': cartItems,
    }
    return render(request, 'main/home.htm' , context)

def profile(request):
    menus = Menu.objects.all()
    categories = Category.objects.all()
    nav_products = Product.objects.all()

    if request.user.is_authenticated:
        customer = request.user.profile
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_item
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_item': 0, 'shipping': False}
        cartItems = order['get_cart_item']


    context = {
        'menus':menus,
        'categories':categories,
        'nav_products':nav_products,
        'items': items,
        'order': order,
        'cartItems': cartItems,
    }
    return render(request, 'account/profile.htm', context)