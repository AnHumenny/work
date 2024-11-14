from django.db import models
from django.db.models import GenericIPAddressField
from tinymce.models import HTMLField


class Fttx(
    models.Model):  # Создаём новый класс, который будет служить для блога моделью, указывая все необходимые элементы.
    city = models.CharField(max_length=30)
    claster = models.CharField(max_length=30)
    street = models.CharField(max_length=40)
    number = models.CharField(max_length=10)
    description = HTMLField()
    askue = GenericIPAddressField()


    def __str__(self):
        return f"{self.city}, {self.street}, {self.number}"

    class Meta:
        verbose_name_plural = "FttxX"  # Указываем правильное написание для множественного числа слова Entry