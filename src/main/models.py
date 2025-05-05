from django.db import models
import uuid
from users.models import Profile, Location
from .constants import CARS_BRANDS, TRANSMISSION_OPTIONS
from .utils import user_listings_path

# Create your models here.
class Listing(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    seller = models.ForeignKey(Profile, on_delete=models.CASCADE)
    brand = models.CharField(max_length=32, choices=CARS_BRANDS, default=None)
    model = models.CharField(max_length=32)
    vin = models.CharField(max_length=32)
    milage = models.IntegerField(default=0)
    color = models.CharField(max_length=32)
    description = models.TextField()
    engine = models.CharField(max_length=32)
    transmission =  models.CharField(max_length=32, choices=TRANSMISSION_OPTIONS, default=None)
    location = models.OneToOneField(Location, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to=user_listings_path)
    

    def __str__(self) -> str:
        return f"{self.seller.user.username}'s Listing - {self.model}"