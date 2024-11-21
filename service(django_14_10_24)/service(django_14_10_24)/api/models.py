from django.db import models
from django.utils import timezone

class Users(models.Model):
    username = models.CharField(max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    class Meta:
        db_table = 'auth_user'
        managed = False

class InfoLastMonth(models.Model):
    date_created = models.DateField(default=timezone.now)
    city = models.CharField(max_length=20)
    street = models.CharField(max_length=30)
    home = models.CharField(max_length=7)
    apartment = models.CharField(max_length=4)
    name = models.CharField(max_length=100)
    class Meta:
        db_table = 'info_info'
        managed = False

class InfoPreviosMonth(InfoLastMonth):
    pass

class SearchKey(models.Model):
    city = models.CharField(max_length=20)
    street = models.CharField(max_length=30)
    home = models.CharField(max_length=7)
    entrance = models.IntegerField()
    ind = models.IntegerField()
    stand = models.IntegerField()
    class Meta:
        db_table = 'key_key'
        managed = False


