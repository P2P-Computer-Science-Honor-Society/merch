from django.shortcuts import render, redirect
from clubs.models import Product
from clubs.forms import CreateProduct
# Create your views here.

def design_ui(response):
    return render(response, "designUI/designer.html")


def create_product(response):
    if response.method == "POST":
        form = CreateProduct(response.POST, response.FILES)
        if form.is_valid():
            cleaned = form.cleaned_data
            user = response.user
            title = cleaned['title']
            printful_link = cleaned['printful_link']
            price = cleaned['price']
            product_image = cleaned['picture']
            profile = Product(title=title, printful_link=printful_link, price=price, picture=product_image)
            profile.save()
            return redirect("/home/")
    else:
        form = CreateProduct()
        return render(response, "designUI/createProduct.html", {"form":form})
