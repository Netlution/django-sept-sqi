from django.urls import path

from . import views

urlpatterns = [
    path("home/", views.new_view, name="home"),
]