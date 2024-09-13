from django.shortcuts import render, redirect
from app.models import * 
from e_commerce.users.models import User
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    product = Product.objects.all().order_by('?')
    context = {
        "product": product,
    }
    return render(request, 'app/home.html', context)
@login_required
def laptop(request):
    category = Category.objects.get(id=1)
    context = {
        "category": category.products.all(),
        # "product": product,
    }
    return render(request, 'app/laptop.html', context)
@login_required
def mobile(request):
    category = Category.objects.get(id=2)
    context = {
        "category": category.products.all(),
    }
    return render(request, 'app/mobile.html', context)
@login_required
def watch(request):
    category = Category.objects.get(id=3)
    context = {
        "category": category.products.all(),
    }
    return render(request, 'app/watch.html', context)

@login_required
def detalis(request, ref):
    product = Product.objects.get(ref=ref)
    context = {
        "product": product,
    }
    return render(request, 'app/detalis.html', context)


@login_required
def cart(request):
    user_cart, created = Cart.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        prodect_ref = request.POST.get("cart")
        prodect = Product.objects.get(ref=prodect_ref)
        user_cart.products.add(prodect)
        return redirect('cart')
    
    products = user_cart.products.all()
    
    context = {
        'prodect': user_cart,
        'products': products
    }
    return render(request, 'app/cart.html', context=context)
    
@login_required
def wishlist(request):
    user_wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        prodect_ref = request.POST.get("wishlist")
        prodect = Product.objects.get(ref=prodect_ref)
        user_wishlist.products.add(prodect)
        return redirect('wishlist')
    
    products = user_wishlist.products.all()
    
    context = {
        'prodect': user_wishlist,
        'products': products
    }
    return render(request, 'app/wishlist.html', context=context)
    

import json
@login_required
def product_buy(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        buy = data['buy']
        
        if True: #Your code to check
            return JsonResponse({'message': 'Product purchased successfully!', 'status': 'success'})
        else: 
            return JsonResponse({'message': 'Invalid JSON', 'status': 'error'}, status=400)

    return JsonResponse({'message': 'Invalid request method', 'status': 'error'}, status=405)

@login_required
def product_search(request):

    query = request.GET.get('q')

    if query:
        results = Product.objects.filter(name__icontains=query)
        print("#"*100)
        print(len(results))
        print("#"*100)
        return render(request, 'app/search.html', {'query': query, 'products': results})
    else:
        return JsonResponse({'error': 'No search query provided'}, status=400)

@login_required
def setting(request):
    return render(request, 'app/settings.html')


def dark_mode(request):
    response = redirect('setting')  # إعادة التوجيه إلى صفحة الإعدادات أو الصفحة المطلوبة

    # التحقق من حالة الكعكة (cookie) الحالية
    dark_mode_status = request.COOKIES.get('dark_mode', 'False') == 'True'
    
    # تبديل حالة الكعكة
    if dark_mode_status:
        response.set_cookie('dark_mode', 'False', max_age=3600*24*7*30)  # تعطيل الوضع الداكن
    else:
        response.set_cookie('dark_mode', 'True', max_age=3600*24*7*30)  # تفعيل الوضع الداكن

    return response