from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("base/", views.base, name="base")
]

urlpatterns += staticfiles_urlpatterns()
