from django.db import models

# Create your models here.

class UserData(models.Model):

    name = models.CharField(max_length = 100)
    age = models.PositiveIntegerField()
    email = models.EmailField()
    address = models.CharField(max_length = 250)
    mobileNo = models.CharField(max_length = 10)
    image = models.ImageField(upload_to = 'media/', blank = True, null = True)
    
