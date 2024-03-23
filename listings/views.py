from django.shortcuts import render
from .models import Listing
# Create your views here.

def listing_list(request):
    listings = Listing.objects.all()
    return render(request, 'lisiting.html', {'listings':listings})

def listing_retrieve(request, id):
    listings = Listing.objects.get(id=id)
    return render(request, 'lisiting.html', {'listings':listings})