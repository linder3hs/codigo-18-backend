from .models import Product, Category  # model
from .serializers import ProductSerializer, CategorySerializer  # serializer
# la clase de rest framework que permite crear un CRUD
from rest_framework.viewsets import ModelViewSet


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
