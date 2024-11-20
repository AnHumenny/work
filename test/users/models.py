from django.db import models
import bcrypt
from django.core.exceptions import ValidationError

def validate_age(value):
    if value < 16 or value > 80:
        raise ValidationError('диапазон 16-80 лет')   #возрастное ограничение

class User(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)         #в дальнейшем используем как логин
    age = models.IntegerField(validators=[validate_age])
    password = models.CharField(max_length=60)  # в хэш

    def set_password(self, raw_password):
        self.password = bcrypt.hashpw(raw_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8') #в хэш

    def check_password(self, raw_password):
        return bcrypt.checkpw(raw_password.encode('utf-8'), self.password.encode('utf-8'))   #из хэша

class Order(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)       #сверка с USER

    def __str__(self):
        return self.title # возвращаем заголовок
