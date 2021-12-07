from django.shortcuts import render

# Create your views here.

def design_ui(response):
    return render(response, "designUI/designer.html")
