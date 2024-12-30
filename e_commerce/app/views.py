from django.shortcuts import render, redirect
from app.models import *
from e_commerce.users.models import User
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    product = Product.objects.all().order_by('?')
    category =  Category.objects.all().only('name')
    context = {
        "product": product,
        "category": category,

    }
    return render(request, 'app/home.html', context)

@login_required
def products(request, slug):
    category = Category.objects.get(slug=slug)
    context = {
        "name": category,
        "category": category.products.all(),
    }
    return render(request, 'app/products.html', context)

@login_required
def detalis(request, ref):
    product = Product.objects.get(ref=ref)
    user = request.user

    if request.method == "POST":
        method = request.POST.get("method")
        action_type = "wishlist" if "wishlist" in request.POST else "cart"
        model_mapping = {
            "wishlist": Wishlist,
            "cart": Cart,
        }

        Model = model_mapping[action_type]
        obj, created = Model.objects.get_or_create(user=user)

        if method.lower() == "post":
            obj.products.add(product)
        elif method.lower() == "delete":
            obj.products.remove(product)


    # Check if the product is in the user's cart
    is_cart = Cart.objects.filter(user=user, products=product).exists()

    # Check if the product is in the user's wishlist
    is_wishlist = Wishlist.objects.filter(user=user, products=product).exists()

    context = {
        "product": product,
        "is_cart": is_cart,
        "is_wishlist": is_wishlist,
    }
    return render(request, 'app/detalis.html', context)


@login_required
def cart(request):
    user_cart = Cart.objects.get(user=request.user)

    products = user_cart.products.all()

    context = {
        'products': products
    }
    return render(request, 'app/cart.html', context=context)


@login_required
def wishlist(request):
    user_wishlist= Wishlist.objects.get(user=request.user)

    products = user_wishlist.products.all()

    context = {
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
