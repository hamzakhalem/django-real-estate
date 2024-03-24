from django.forms import ModelForm
from .models import Listing

class ListingFrom(ModelForm):
    class Meta: 
        model = Listing
        fields  = ['title', 'price']