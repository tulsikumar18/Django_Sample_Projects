from django.db import models

# Create your models here.

class car(models.Model):

    name = models.CharField(max_length=12)
    year = models.PositiveIntegerField()
    seater = models.PositiveBigIntegerField()
    fuel_type = models.CharField(max_length=12)
    milage = models.IntegerField()
    cc = models.PositiveIntegerField()
    country_origin = models.CharField(max_length=12)


# class student(models.Model):

#     Name = models.CharField(max_length=10)
#     age = models.PositiveIntegerField()