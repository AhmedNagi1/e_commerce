from django.shortcuts import render
from app.models import * 
category = Category.objects.get(id=3)

# حذف جميع المنتجات المرتبطة بهذه الفئة
def home(request):
    product = Product.objects.all().order_by('?')
    context = {
        "product": product,
    }
    return render(request, 'app/home.html', context)

def laptop(request):
    category = Category.objects.get(id=1)
    context = {
        "category": category.products.all(),
        # "product": product,
    }
    return render(request, 'app/laptop.html', context)

def mobile(request):
    category = Category.objects.get(id=2)
    context = {
        "category": category.products.all(),
    }
    return render(request, 'app/mobile.html', context)

def watch(request):
    category = Category.objects.get(id=3)
    context = {
        "category": category.products.all(),
    }
    return render(request, 'app/watch.html', context)

def detalis(request, ref):
    product = Product.objects.get(ref=ref)
    context = {
        "product": product,
    }
    return render(request, 'app/detalis.html', context)


# def home(request):
#     category = Category.objects.all()
#     product = Product.objects.all()
#     context = {
#         # "category": category,
#         "product": product,
#     }
#     return render(request, 'app/home.html', context)
# def home(request):
#     category = Category.objects.all()
#     product = Product.objects.all()
#     context = {
#         # "category": category,
#         "product": product,
#     }
#     return render(request, 'app/home.html', context)
