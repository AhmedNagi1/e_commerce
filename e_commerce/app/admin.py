from django.contrib import admin
from .models import Product, Category



@admin.register(Category)
class CategorytAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'description']
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']
