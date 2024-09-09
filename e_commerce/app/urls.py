from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('laptop/', views.laptop, name='laptop'),
    path('mobile/', views.mobile, name='mobile'),
    path('watch/', views.watch, name='watch'),
    path('detalis/<uuid:ref>', views.detalis, name='detalis'),
    path('cart/', views.cart, name='cart'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('product_buy/', views.product_buy, name='product_buy'),
]
