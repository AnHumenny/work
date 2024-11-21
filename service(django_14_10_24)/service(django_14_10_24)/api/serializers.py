from rest_framework import serializers
from .models import InfoLastMonth, Users, SearchKey

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'username', 'first_name', 'last_name', 'email']

class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoLastMonth
        fields = ['id', 'date_created', 'city', 'street', 'home', 'apartment', 'name']

class InfoSerializerPrevios(InfoSerializer):
    pass

class KeySerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchKey
        fields = ['id', 'city', 'street', 'home', 'entrance', 'ind', 'stand']