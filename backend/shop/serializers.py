from rest_framework import serializers
from .models import Product,Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

# для регситрации пользователя мы передадим поля модели напрямую в самом сериалайзере в целях защиты данных

class SimpleUserSerializer(serializers.ModelSerializer):
    id = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()


class ProductSerializer(serializers.ModelSerializer):
    # Если мы вкладываем в класс сериализатора новые данные других сериалайзеров 
    # то есть помещаем новые словарики внутрь основного  словаря
    # мы обязаны передать их до объявления класса Meta:
    # после объявления class Meta
    # мы можем добавить небольшую логику (методы класса)
    # Вкладываем данные владельца
    owner_info = SimpleUserSerializer(source = 'owner',read_only = True)
    # вкладываем данные категории 
    # category_name = Category(source = 'category',read_only=True)
    category_name2 = serializers.CharField(source = 'category.name',read_only = True)

    # если вдруг мы захотели добавить вычесляемое поле с математическими операциями 
    is_expensive = serializers.SerializerMethodField()
    # допустим написали все вложенные сериалайзеры

    class Meta:
        model = Product
        fields = ['id','name','price','category','category_name2','owner','owner_info','is_expensive']
    # создадим метод для нашего is_expensive
    def get_is_expensive(self,obj):
        return obj.price > 1000