# Create your models here.
from django.db import models
from django.utils import timezone


class Key(
    models.Model):  # Создаём новый класс, который будет служить для блога моделью, указывая все необходимые элементы.
    city = models.CharField(max_length=20)
    street = models.CharField(max_length=30)
    home = models.CharField(max_length=7)
    entrance = models.IntegerField()
    ind = models.IntegerField()
    stand = models.IntegerField()


    def __str__(self):  # С помощью функции меняем то, как будет представлена запись в модели.
        return self.city   # Указываем, что она будет идентифицироваться с помощью своего заголовка.

    class Meta:
        verbose_name_plural = "Key_s"  # Указываем правильное написание для множественного числа слова Entry