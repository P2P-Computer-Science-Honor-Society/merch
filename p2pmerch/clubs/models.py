from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.TextField(default=None)
    printful_link = models.TextField(default=None)
    price = models.FloatField(default=None)
    picture = models.ImageField(upload_to="product_pictures", blank=True)

    @property
    def safe_img_url(self):
        if self.picture:
            return self.picture.url
        else:
            return "/media/product_pictures/defaultproduct.jpg"
