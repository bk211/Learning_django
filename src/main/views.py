from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

from .models import Listing

def main_view(request):
    return render(request, "views/main.html", {"name": "home"})

@login_required
def home_view(request):
    listings = Listing.objects.all()
    context = {
        'listings' : listings,
    }
    return render(request, "views/home.html", context)

