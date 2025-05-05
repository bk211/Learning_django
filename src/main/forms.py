from django import forms
from .models import Listing

class ListingForm(forms.ModelForm):
    image = forms.ImageField(required=True)

    class Meta:
        model = Listing
        fields = {'brand', 'model', 'vin', 'milage',
                  'color', 'description', 'engine', 'transmission', 'image'}