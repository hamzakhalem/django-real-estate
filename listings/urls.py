from django.contrib import admin
from django.urls import path
from .views import listing_list
urlpatterns = [
    path('', listing_list, name='listing')
]
