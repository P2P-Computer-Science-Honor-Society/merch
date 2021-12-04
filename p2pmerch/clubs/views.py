from django.shortcuts import render

# Create your views here.

def base_club(response):
    return render(response, "clubs/baseClub.html")
