from django.contrib import admin
from .models import Product, Category, Cart, Wishlist



@admin.register(Category)
class CategorytAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'description']
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']
    
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user']
    
@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ['user']
