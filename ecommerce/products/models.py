from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    category_name = models.CharField(max_length=1000, blank=False, default=0, null=True)

    def __str__(self):
        return self.category_name

class Product(models.Model):
    product_name = models.CharField(max_length=100, null=False, blank=False, default='')
    product_description = models.CharField(max_length=1000, null=False, blank=False, default='')
    product_price = models.IntegerField()
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_image = models.URLField(default='https://i0.wp.com/post.healthline.com/wp-content/uploads/2020/10/689927-cbdMD-Products-2020-Review-1296x728-Header-c0dcdf.jpg?w=1155&h=1528')

    def __str__(self):
        return self.product_name

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.user.username


class CartItem(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0, blank=False)
    date_added = models.DateField(auto_now_add=True)
    @property
    def get_total(self):
        price = self.product.product_price * self.quantity
        return price

    def __str__(self):
        return self.product.product_name
