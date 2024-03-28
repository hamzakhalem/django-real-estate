from django.contrib import admin
from django.urls import path
from .views import listing_list, listing_retrieve, listing_create,listing_update, listing_delete
urlpatterns = [
    path('', listing_list, name='listing'),
    path('listing/<pk>/', listing_retrieve, name='listing-show'),
    path('listing-update/<pk>/', listing_update, name='listing-update'),
    path('listing-delete/<pk>/', listing_delete, name='listing-delete'),
    path('listing-create/', listing_create, name='listing-create')
]
