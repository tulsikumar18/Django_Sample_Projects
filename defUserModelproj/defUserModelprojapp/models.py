from django.db import models

from django.contrib.auth.models import User

# Create your models here.



class UserDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ## additional fields..
    phone = models.BigIntegerField()
    age = models.PositiveIntegerField()
    house_no = models.IntegerField()
    street = models.CharField(max_length = 100)
    address = models.CharField(max_length = 100)
    city = models.CharField(max_length = 50)
    state = models.CharField(max_length = 50)
    zipcode = models.IntegerField()
    userpic = models.ImageField(upload_to ='userpic/', blank = True, null = True)





