from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

from .models import Listing
from .forms import ListingForm
from users.forms import LocationForm

def main_view(request):
    return render(request, "views/main.html", {"name": "home"})

@login_required
def home_view(request):
    listings = Listing.objects.all()
    context = {
        'listings' : listings,
    }
    return render(request, "views/home.html", context)

@login_required
def list_view(request):
    if request.method == "POST":
        pass
    elif request.method == "GET":
        listingForm = ListingForm()
        locationForm = LocationForm()

    return render(request, 'views/list.html', 
    {'listing_form': listingForm, 
        'location_form': locationForm
    })