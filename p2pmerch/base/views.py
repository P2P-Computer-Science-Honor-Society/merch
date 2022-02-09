from django.shortcuts import render

def base(response):
    return render(response, "base/base.html")

def home(response):
    return render(response, "base/home.html")

def login(response):
    return render(response, "base/login.html")

def test(response):
    return render(response, "base/test.html")