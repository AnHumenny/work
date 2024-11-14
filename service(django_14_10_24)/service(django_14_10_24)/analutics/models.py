from django.db import models


class Analutic(
    models.Model):
    date_created = models.DateField()
    city = models.CharField(max_length=20)
    street = models.CharField(max_length=30)