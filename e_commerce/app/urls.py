from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('products/<slug:slug>', views.products, name='products'),
    path('detalis/<uuid:ref>', views.detalis, name='detalis'),
    path('cart/', views.cart, name='cart'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('product_buy/', views.product_buy, name='product_buy'),
    path('search/', views.product_search, name='product_search'),
    path('setting/', views.setting, name='setting'),
    path('dark_mode/', views.dark_mode, name='dark_mode'),
]
