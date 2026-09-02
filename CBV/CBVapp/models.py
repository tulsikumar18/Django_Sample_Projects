from django.db import models

from django.urls import reverse

# Create your models here.


class Company(models.Model):
    name=models.CharField(max_length=100)
    ceo = models.CharField(max_length=100)
    logo = models.ImageField(upload_to = 'logo/', blank = True, null = True)
    est_year = models.IntegerField()
    origin = models.CharField(max_length=100)


    # used to diplay the name instead of objects in the admin panel..
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('company-detail', kwargs={'pk': self.pk})



fuels = [

    ('PETROL', 'petrol'),
    ('DIESEL', 'diesel'),
    ('EV', 'ev')
]

class Products(models.Model):

    prod_name = models.CharField(max_length = 100)
    price = models.IntegerField()

    prod_img = models.ImageField(upload_to = 'prodImg/', blank = True, null = True)
    color = models.CharField(max_length=100)
    engine_cc = models.CharField(max_length = 100)
    fuel_type = models.CharField(max_length = 100, choices = fuels)

    mileage = models.CharField(max_length = 100)
    seating = models.IntegerField()
    company=models.ForeignKey(Company, related_name='companies', on_delete=models.CASCADE)


    # used to diplay the name instead of objects in the admin panel..
    def __str__(self):
        return self.prod_name
    