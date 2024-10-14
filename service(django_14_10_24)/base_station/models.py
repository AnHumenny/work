# Create your models here.
from django.db import models
from django.utils import timezone


class BaseStation(
    models.Model): 
    number = models.IntegerField()
    city = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    comment = models.CharField(max_length=255)


    def __str__(self):  
        return self.city   

    class Meta:
        verbose_name_plural = "BaseStations"  
