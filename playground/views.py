from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product


def say_hello(request):
    # Keyword=value
    queryset = Product.objects.filter(inventory__lt='10')       
    
    return render(request, 'hello.html', {'name': 'Mosh', 'products': list(queryset)})
