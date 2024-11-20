from rest_framework.exceptions import ValidationError
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Order, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'age', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])  # Хранить пароль в зашифрованном виде
        user.save()
        return user

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'title', 'description', 'price', 'user']

    def create(self, validated_data):
        user_id = validated_data.get('user').id
        if not User.objects.filter(id=user_id).exists():
            raise ValidationError("Пользователь с таким ID не существует.")
        return super().create(validated_data)
