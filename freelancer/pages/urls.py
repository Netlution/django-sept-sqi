from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='services'),
    path("Testimonials/", views.about, name='testimonials'),
    path("Cases/", views.contact, name='Cases'),
    path("Blog/", views.contact, name='Blog'),
    path("Pricing/", views.contact, name='Pricing'),
]