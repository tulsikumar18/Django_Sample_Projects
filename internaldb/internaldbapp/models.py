from django.db import models

# Create your models here.

class STUDENT(models.Model):

    usn = models.CharField(max_length = 20)
    name = models.CharField(max_length = 100)
    age = models.PositiveBigIntegerField()
    marks = models.IntegerField()
    email = models.EmailField()
    grade = models.CharField(max_length = 10)
    degree = models.CharField(max_length = 10)


    ## to display the name instead of the object..use ___str__ method..UserWarning

    def __str__(self):
        return self.name


    
