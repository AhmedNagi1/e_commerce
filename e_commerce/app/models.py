from django.db import models
import random
import uuid
from e_commerce.users.models import User
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    ref = models.UUIDField(default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(User, related_name='cart', on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, related_name='carts')
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def total_price(self):
        return sum(product.price for product in self.products.all())

    def __str__(self):
        return f"Cart of {self.user.username}"

class Wishlist(models.Model):
    user = models.ForeignKey(User, related_name='wishlist', on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, related_name='wishlists')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Wishlist of {self.user.username}"


class ProdectBuy(models.Model):
    user = models.ForeignKey(User, related_name='buy', on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, related_name='buy')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"prodec buy of {self.user.username}"
