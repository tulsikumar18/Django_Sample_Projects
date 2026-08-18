
from django.db import models

# Create your models here.

CATEGORY_CHOICES = [
    ('BREAKFAST', 'breakfast'),
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
    is_available = models.BooleanField(default=True)



    