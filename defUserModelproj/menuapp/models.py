
from defUserModelprojapp.models import VendorDetails
from django.db import models

# Create your models here.

CATEGORY_CHOICES = [
    ('BREAKFAST', 'breakfast'),
    ('STARTERS', 'starters'),
    ('LUNCH', 'lunch'),
    ('DINNER', 'dinner'),
    ('BEVERAGES', 'beverages'),
    ('DESSERTS', 'desserts'),
    
]


class FoodItems(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    img = models.ImageField(upload_to='foodimg/', blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    vendor = models.ForeignKey(VendorDetails, related_name='vendorDetailss' , on_delete=models.CASCADE)  
    # this we are using such that only the food items added for the required vendor only..
    # on_delete=models.CASCADE means if vendor is deleted then all food items of that vendor will be deleted.
    is_available = models.BooleanField(default=True)



    