from rest_framework.viewsets import ModelViewSet
from .models import Category, Task
from .serializers import CategorySerializer, TaskSerializer
from users.utils import validate_token
from rest_framework.response import Response


# Primero haremos el CURD para Category
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def list(self, request):
        header = request.headers.get('Authorization')
        if header is None:
            return Response({
                "message": "Token is required"
            })

        if not validate_token(header.split()[1]):
            return Response({
                "message": "Token no valid"
            })
        queryset = TaskSerializer(Task.objects.all(), many=True).data
        return Response(queryset)
