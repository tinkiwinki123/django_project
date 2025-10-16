from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    color = models.TextField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    brand = models.CharField(max_length=20)
    dev_country = models.CharField(max_length=20)
    image = models.ImageField(upload_to='products/', null=True)

def __str__(self):
        return f"{self.brand}  {self.name}"

class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(null=True, blank=True)
    amount_of_products = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    #products = models.ManyToManyField(Product, through='OrderItem')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('canceled', 'Canceled')
    ], default='pending')
   

    