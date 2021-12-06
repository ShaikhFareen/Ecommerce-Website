from django.shortcuts import render
from django.http import JsonResponse
from .models import Category, Product, CartItem
import json
from .forms import SignupForm
from django.contrib import messages

def product_view(request):
    products = Product.objects.all()
    
    categories = Category.objects.all()
    params =  {'products':products, 'categories':categories}
    return render(request, 'home.html', params)

def cart_view(request):
    cart_items = CartItem.objects.all()
    categories = Category.objects.all()
    params = {'cartitems':cart_items,'categories':categories}
    return render(request, 'cart.html', params)

def updateitem_view(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    product= Product.objects.get(id=productId)
    cart_items, created = CartItem.objects.get_or_create(product=product)
    if action == 'add':
       cart_items.quantity = (cart_items.quantity + 1)
    elif action == 'remove':
        cart_items.quantity = (cart_items.quantity - 1)
    cart_items.save()

    if cart_items.quantity < 1:
        cart_items.delete()
    return JsonResponse("Item added sucessfully", safe=False)

def SignUp_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully registered.Please Login to continue')
    else:
        form = SignupForm()
    categories = Category.objects.all()
    params = {'form':form ,'title':'SignUp','categories':categories}
    return render(request, 'signup.html', params)

def logout_view(request):
    pass

def category_view(request, pk):
    categories = Category.objects.all()
    category = Category.objects.filter(pk=pk)
    products = Product.objects.filter(product_category=category[0])
    params = {'products':products,'categories':categories, 'title':'Category-wise'}
    return render(request, 'category.html', params)
