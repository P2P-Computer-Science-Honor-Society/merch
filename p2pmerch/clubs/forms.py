from django import forms
import datetime as dt
from .models import Product
from django.utils.safestring import mark_safe

class UploadImage(forms.ModelForm):
    picture = forms.ImageField(label = "Product Picture", required=False)

    class Meta:
        model = Product
        fields = ['picture']

class CreateProduct(forms.Form):
    title = forms.CharField(max_length=50, widget=forms.TextInput())
    printful_link = forms.URLField(label= "Printful Product Link", max_length=300)
    price = forms.FloatField(label = "Price", required=False)
    picture = forms.ImageField(label = "Product Picture", required=False)