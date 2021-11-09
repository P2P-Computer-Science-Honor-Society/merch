from django.shortcuts import render

def base(response):
    return render(response, "base/base.html")