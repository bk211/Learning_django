from django import forms
from .models import Location
from localflavor.us.models import USZipCodeField

class LocationForm(forms.ModelForm):


    adress_1 = forms.CharField(required=False)
    zip_code = USZipCodeField(blank=True)

    class Meta:
        model = Location
        fields = {'adress_1', 'adress_2', 'city', 'state', 'zip_code'}