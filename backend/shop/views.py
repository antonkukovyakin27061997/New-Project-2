from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.select_related('owner','category')
    serializer_class = ProductSerializer


    # если хотим получить все данные за один запрос 
    # создадим отдельные метод для этого
    def get_queryset(self):
        return Product.objects.select_related('owner','category').all()

class ProductDetailAPIview(generics.RetrieveAPIView):
    queryset = Product.objects.select_related('owner','category')
    serializer_class = ProductSerializer

# Что нам это дало по заключению 
# 1 - Один запрос = все данные
# 2 - нет N+1 проблемы
# 3 - чистая структура 
# 4 - можно расширять


