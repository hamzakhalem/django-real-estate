from django.contrib import admin
from django.urls import path
from .views import listing_list, listing_retrieve, listing_create
urlpatterns = [
    path('', listing_list, name='listing'),
    path('listing/<pk>/', listing_retrieve, name='listing-show'),
    path('listing-create/', listing_create, name='listing-create'),
]
