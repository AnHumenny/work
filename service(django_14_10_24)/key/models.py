from django.db import models
from django.utils import timezone


class Key(
    models.Model): 
    city = models.CharField(max_length=20)
    street = models.CharField(max_length=30)
    home = models.CharField(max_length=7)
    entrance = models.IntegerField()
    ind = models.IntegerField()
    stand = models.IntegerField()


    def __str__(self): 
        return self.city   

    class Meta:
        verbose_name_plural = "Key_s"  
