from django.shortcuts import render
from store.models import Product


def say_hello(request):
    product = Product.objects.get(pk=2)
    print(product)  
    
    return render(request, 'hello.html', {'name': 'Mosh'})
