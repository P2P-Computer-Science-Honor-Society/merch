from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("ui/", views.design_ui, name="ui"),
]

urlpatterns += staticfiles_urlpatterns()
