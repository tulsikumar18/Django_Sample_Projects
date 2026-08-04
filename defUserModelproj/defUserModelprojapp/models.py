from django.db import models


from django.contrib.auth.models import User

# Create your models here.

class UserDetails(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)


## additional fields..


class UserDetails(models.Model):

    phone = models.BigIntegerField()
    age = models.PositiveIntegerField()
    house_no = models.IntegerField()
    address = models.CharField(max_length = 100)
    city = models.CharField(max_length = 50)
    userpic = models.ImageField(upload_to ='userpic/', null = True, blank = True)
    




