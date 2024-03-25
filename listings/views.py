from django.shortcuts import render, redirect
from .models import Listing
from .forms import ListingFrom
# Create your views here.

def listing_list(request):
    listings = Listing.objects.all()
    return render(request, 'lisitings.html', {'listings':listings})

def listing_retrieve(request, pk):
    listing = Listing.objects.get(id=pk)
    return render(request, 'listing.html', {'listing':listing})

def listing_create(request):
    form = ListingFrom()
    if request.method == 'POST':
        form = ListingFrom(request.POST)
        if form.is_valid:
            form.save()
            return redirect('listing')
    return render(request, 'listing-create.html', {'form':form})