from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("", views.base_product, name="product"),
]

urlpatterns += staticfiles_urlpatterns()
