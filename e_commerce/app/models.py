from django.db import models
import random
import uuid
from e_commerce.users.models import User
from django.utils.text import slugify

class Category(models.Model):
    """
    Model representing a product category.

    Attributes:
        name (CharField): The name of the category.
        description (TextField): A description of the category.
        slug (SlugField): A unique slug for the category, generated from the name.
    """

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        """
        Save method override to generate a slug from the name if not provided.
        """
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        """
        String representation of the Category.
        """
        return self.name

class Product(models.Model):
    """
    Model representing a product.

    Attributes:
        name (CharField): The name of the product.
        description (TextField): A description of the product.
        price (DecimalField): The price of the product.
        stock (PositiveIntegerField): The stock quantity of the product.
        category (ForeignKey): The category to which the product belongs.
        image (ImageField): An optional image of the product.
        ref (UUIDField): A unique reference for the product.
    """

    name = models.CharField(max_length=100, db_index=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    ref = models.UUIDField(default=uuid.uuid4, editable=False)

    def __str__(self):
        """
        String representation of the Product.
        """
        return self.name

class Cart(models.Model):
    """
    Model representing a shopping cart.

    Attributes:
        user (ForeignKey): The user who owns the cart.
        products (ManyToManyField): The products in the cart.
        created_at (DateTimeField): The date and time when the cart was created.
    """

    user = models.ForeignKey(User, related_name='cart', on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, related_name='carts')
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def total_price(self):
        """
        Calculate the total price of all products in the cart.
        """
        return sum(product.price for product in self.products.all())

    def __str__(self):
        """
        String representation of the Cart.
        """
        return f"Cart of {self.user.username}"

class Wishlist(models.Model):
    """
    Model representing a wishlist.

    Attributes:
        user (ForeignKey): The user who owns the wishlist.
        products (ManyToManyField): The products in the wishlist.
        created_at (DateTimeField): The date and time when the wishlist was created.
    """

    user = models.ForeignKey(User, related_name='wishlist', on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, related_name='wishlists')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        String representation of the Wishlist.
        """
        return f"Wishlist of {self.user.username}"

class ProdectBuy(models.Model):
    """
    Model representing a product purchase.

    Attributes:
        user (ForeignKey): The user who made the purchase.
        products (ManyToManyField): The products purchased.
        created_at (DateTimeField): The date and time when the purchase was made.
    """

    user = models.ForeignKey(User, related_name='buy', on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, related_name='buy')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        String representation of the ProdectBuy.
        """
        return f"prodec buy of {self.user.username}"
