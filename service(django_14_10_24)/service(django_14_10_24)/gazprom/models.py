# Create your models here.
from django.db import models
from tinymce.models import HTMLField


class Gazprom(
    models.Model):  # Создаём новый класс, который будет служить для блога моделью, указывая все необходимые элементы.
    ip = models.CharField(max_length=14)
    number = models.CharField(max_length=10)
    address = models.CharField(max_length=255)
    type = models.CharField(max_length=30)
    region = models.CharField(max_length=255)
    comment = HTMLField()
    geo = models.CharField(max_length=50)

    def __str__(self):  # С помощью функции меняем то, как будет представлена запись в модели.
        return self.geo# Указываем, что она будет идентифицироваться с помощью своего заголовка.

    class Meta:
        verbose_name_plural = "Gazproms"  # Указываем правильное написание для множественного числа слова Entry