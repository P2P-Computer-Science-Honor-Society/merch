from django.shortcuts import render

# Create your views here.

def base_product(response):
    return render(response, "products/baseProduct.html")
