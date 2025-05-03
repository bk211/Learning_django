from django.db import models
from django.contrib.auth.models import User
from localflavor.us.models import USStateField, USZipCodeField
from .utils import user_directory_path

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=user_directory_path, null=True)
    bio = models.CharField(max_length=140, blank=True)
    phone_number = models.CharField(max_length=22, blank=True)
    location = models.OneToOneField('users.Location', on_delete=models.SET_NULL, null=True)
    
    def __str__(self) -> str:
        return f"{self.user.username}'s Profile"

class Location(models.Model):
    adress_1 = models.CharField(max_length=33)
    adress_2 = models.CharField(max_length=33, blank=True)
    city = models.CharField(max_length=64)
    state = USStateField(default="NY")
    zip_code = USZipCodeField(blank=True)

    def __str__(self) -> str:
        return f"{self.id}'s Location"