from .models import Product  # model
from .serializers import ProductSerializer  # serializer
# la clase de rest framework que permite crear un CRUD
from rest_framework.viewsets import ModelViewSet


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
