from django.urls import path

from . import views

urlpatterns = [
    path("about/", views.new_view, name="about"),
]