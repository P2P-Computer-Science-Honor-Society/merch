from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("cshs/", views.base_club, name="cshs"),
]

urlpatterns += staticfiles_urlpatterns()
