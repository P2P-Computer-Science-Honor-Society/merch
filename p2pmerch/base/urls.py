from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("", views.base, name="base"),
    path("home/", views.base, name="base"),
]

urlpatterns += staticfiles_urlpatterns()
