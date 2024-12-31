from django.shortcuts import render, redirect
from app.models import *
from e_commerce.users.models import User
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q

@login_required
def home(request):
    """
    Render the home page with all products and categories.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered home page.
    """
    product = Product.objects.all().order_by('?')
    category = Category.objects.all().only('name')
    context = {
        "product": product,
        "category": category,
    }
    return render(request, 'app/home.html', context)

@login_required
def products(request, slug):
    """
    Render the products page for a specific category.

    Args:
        request (HttpRequest): The HTTP request object.
        slug (str): The slug of the category.

    Returns:
        HttpResponse: The rendered products page.
    """
    category = Category.objects.get(slug=slug)
    context = {
        "name": category,
        "category": category.products.all(),
    }
    return render(request, 'app/products.html', context)

@login_required
def detalis(request, ref):
    """
    Render the details page for a specific product and handle wishlist/cart actions.

    Args:
        request (HttpRequest): The HTTP request object.
        ref (str): The reference of the product.

    Returns:
        HttpResponse: The rendered details page.
    """
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

    is_cart = Cart.objects.filter(user=user, products=product).exists()
    is_wishlist = Wishlist.objects.filter(user=user, products=product).exists()

    context = {
        "product": product,
        "is_cart": is_cart,
        "is_wishlist": is_wishlist,
    }
    return render(request, 'app/detalis.html', context)

@login_required
def cart(request):
    """
    Render the cart page for the current user.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered cart page.
    """
    user_cart = Cart.objects.get(user=request.user)
    products = user_cart.products.all()
    context = {
        'products': products,
        'cart': user_cart
    }
    return render(request, 'app/cart.html', context=context)

@login_required
def wishlist(request):
    """
    Render the wishlist page for the current user.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered wishlist page.
    """
    user_wishlist= Wishlist.objects.get(user=request.user)
    products = user_wishlist.products.all()
    context = {
        'products': products
    }
    return render(request, 'app/wishlist.html', context=context)

@login_required
def product_buy(request):
    """
    Handle the product purchase action.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse: The response with success or error message.
    """
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
    """
    Handle the product search action.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse or JsonResponse: The rendered search results page or error message.
    """
    query = request.GET.get('q')

    if query:
        results = Product.objects.filter(
            Q(name__icontains=query)
        )
        return render(request, 'app/search.html', {'query': query, 'products': results})
    else:
        return JsonResponse({'error': 'No search query provided'}, status=400)

@login_required
def setting(request):
    """
    Render the settings page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered settings page.
    """
    return render(request, 'app/settings.html')

def dark_mode(request):
    """
    Toggle dark mode setting.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponseRedirect: Redirect to the settings page.
    """
    response = redirect('setting')  # إعادة التوجيه إلى صفحة الإعدادات أو الصفحة المطلوبة

    # التحقق من حالة الكعكة (cookie) الحالية
    dark_mode_status = request.COOKIES.get('dark_mode', 'False') == 'True'

    # تبديل حالة الكعكة
    if dark_mode_status:
        response.set_cookie('dark_mode', 'False', max_age=3600*24*7*30)  # تعطيل الوضع الداكن
    else:
        response.set_cookie('dark_mode', 'True', max_age=3600*24*7*30)  # تفعيل الوضع الداكن

    return response
