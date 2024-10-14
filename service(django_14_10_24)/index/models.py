# Create your models here.
from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField

class Index(
    models.Model):  # Создаём новый класс, который будет служить для блога моделью, указывая все необходимые элементы.
    title = models.CharField(max_length=500)
    content = HTMLField()
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):  # С помощью функции меняем то, как будет представлена запись в модели.
        return self.title  # Указываем, что она будет идентифицироваться с помощью своего заголовка.

    class Meta:
        verbose_name_plural = "Index_x"  # Указываем правильное написание для множественного числа слова Entry