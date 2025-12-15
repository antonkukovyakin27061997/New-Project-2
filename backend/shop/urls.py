from django.urls import path,include
from .views import ProductListAPIView,ProductDetailAPIview

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

# router.register('products/',ProductListAPIView)
# router.register('products/<int:pk>/',ProductDetailAPIview)

# urlpatterns = [
#     path('',include(router.urls))
# ]

urlpatterns = [
    path('products/',ProductListAPIView.as_view(),name='product-list'),
    path('products/<int:pk>/',ProductDetailAPIview.as_view(),name ='product-detail'),
]