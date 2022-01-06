from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("ui/", views.design_ui, name="ui"),
    path("product/", views.create_product, name="product")
]

urlpatterns += staticfiles_urlpatterns()
