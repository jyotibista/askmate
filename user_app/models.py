from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class UserModel(models.Model):
    username =models.CharField(max_length=50)
    address = models.CharField(max_length= 120) 
    contact = models.IntegerField()
    email = models.CharField(max_length=50)
    password =models.CharField(max_length= 50)
    repuation = models.PositiveIntegerField(validators =[MinValueValidator(0)])

    def __str__(self):
        return (self.username)




    