from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from store.models import Product


def say_hello(request):
    # Proudcts: 0, 1, 2, 3, 4
    queryset = Product.objects.all()[5:10]       
    
    return render(request, 'hello.html', {'name': 'Mosh', 'products': list(queryset)})
