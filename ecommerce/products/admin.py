from django.contrib import admin
from .models import Product, Category, CartItem, Customer

admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(CartItem)
