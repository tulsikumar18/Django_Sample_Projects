
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



class VendorDetails(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='vendor')

    vendor_name = models.CharField(max_length=100)
    vendor_email = models.EmailField()

    restaurant_name = models.CharField(max_length=100)
    phone_no = models.BigIntegerField()
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.IntegerField()

    gst_no = models.CharField(max_length=15)
    license_img = models.ImageField(upload_to='license/',blank=True,null=True )
    restaurant_img = models.ImageField(upload_to='restaurant/',blank=True,null=True)
    is_approved = models.BooleanField(default=False)




