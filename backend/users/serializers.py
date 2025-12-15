from rest_framework import serializers
from .models import User
from shop.serializers import ProductSerializer

# Получаем все товары пользователя в одном запросе 
class UserSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['id','username','email','phone','product']
        