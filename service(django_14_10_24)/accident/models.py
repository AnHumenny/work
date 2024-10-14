# Create your models here.
from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField


class Accident(
    models.Model):  # Создаём новый класс, который будет служить для блога моделью, указывая все необходимые элементы.
    number = models.CharField(max_length=10)
    category = models.CharField(max_length=20)
    sla = models.CharField(max_length=20)
    datetime_open = models.DateTimeField(default=timezone.now)
    datetime_close = models.DateTimeField(default=timezone.now)
    problem = HTMLField()
    city = models.CharField(max_length=255)
    address = models.CharField(max_length=500)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    subscriber = models.CharField(max_length=13)
    comment = HTMLField()
    decide = HTMLField()
    status = models.CharField(max_length=5)

    def __str__(self):  
        return self.number   

    class Meta:
        verbose_name_plural = "Accidents"  
