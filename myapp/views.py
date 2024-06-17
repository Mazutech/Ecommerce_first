from django.shortcuts import render
from .models import Product

# Create your views here.
# from django.http import HttpResponse

def product_list(request):
    products = Product.objects.all()
    context = {
        'products':products
    }
    return render(request, 'myapp/product_list.html', context)