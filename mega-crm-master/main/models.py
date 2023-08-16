from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    desc = models.CharField(max_length=500, null=True, blank=True)
    price = models.DecimalField(blank=True, default=0.00, decimal_places=2, max_digits=7)
    image = models.ImageField(null=True, blank=True, upload_to='media/products/', default='media/products/placeholder.jpeg')
    tags = models.ManyToManyField('Tag', blank=True, related_name='products')
    quantity = models.IntegerField(default=0)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    products = models.ManyToManyField(Product)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'By: {self.user} at {self.time}'

class Cart(models.Model):
    products = models.ManyToManyField(Product)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f' Cart By: {self.user}'

class Saved(models.Model):
    products = models.ManyToManyField(Product)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f' Saved By: {self.user}'

class Save(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product} Saved By: {self.user}'

class Activity(models.Model):
    desc = models.CharField(max_length=600, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.desc} By: {self.user} at {self.time}'
