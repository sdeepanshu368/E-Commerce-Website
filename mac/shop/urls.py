from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("about/", views.about, name="AboutUs"),
    path("checkout/", views.checkout, name="Checkout"),
    path("contact/", views.contact, name="ContactUs"),
    path("products/<int:myid>", views.productView, name="ProductView"),
    path("search/", views.search, name="Search"),
    path("tracker/", views.tracker, name="TrackingStatus"),
]
