from django.db import models


class UserInfo(models.Model):
    name = models.CharField(max_length = 20)
    age = models.PositiveBigIntegerField()
    address = models.CharField(max_length = 100)
    image = models.ImageField(upload_to = 'media/', null = True, blank = True)
