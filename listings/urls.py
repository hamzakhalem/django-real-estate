from django.contrib import admin
from django.urls import path
from .views import listing_list, listing_retrieve
urlpatterns = [
    path('', listing_list, name='listing'),
    path('listing/<pk>/', listing_retrieve, name='listing'),
]
