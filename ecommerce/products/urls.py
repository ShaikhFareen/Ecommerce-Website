from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_view, name="home"),
    path('cart', views.cart_view, name='cart' ),
    path('update_item', views.updateitem_view, name='update_item' ),
    path('signUp', views.SignUp_view, name='signUp' ),
    path('category/<int:pk>', views.category_view, name='category' ),
]