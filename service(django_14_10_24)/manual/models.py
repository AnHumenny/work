# Create your models here.
from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField


class Manual(
    models.Model): 
    type = models.CharField(max_length=20)
    model = models.CharField(max_length=100)
    description = HTMLField()

    def __str__(self):  
        return self.model   

    class Meta:
        verbose_name_plural = "Manuals"  
