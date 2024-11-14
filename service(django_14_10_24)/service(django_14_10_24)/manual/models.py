# Create your models here.
from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField


class Manual(
    models.Model):  # Создаём новый класс, который будет служить для блога моделью, указывая все необходимые элементы.
    type = models.CharField(max_length=20)
    model = models.CharField(max_length=100)
    description = HTMLField()

    def __str__(self):  # С помощью функции меняем то, как будет представлена запись в модели.
        return self.model   # Указываем, что она будет идентифицироваться с помощью своего заголовка.

    class Meta:
        verbose_name_plural = "Manuals"  # Указываем правильное написание для множественного числа слова Entry