from rest_framework.viewsets import ModelViewSet
from .models import Category, Task
from .serializers import CategorySerializer, TaskSerializer
from users.utils import validate_token, get_payload_from_token
from rest_framework.response import Response
from users.models import User
from users.serializers import UserSerializer


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
        token_from_client = header.split()[1]
        if not validate_token(token_from_client):
            return Response({
                "message": "Token no valid"
            })

        payload = get_payload_from_token(token_from_client)
        print(payload.get('user_id'))
        # vamos a buscar al usuario por id
        user = UserSerializer(User.objects.get(pk=payload.get('user_id'))).data

        if not user.get('is_super_user'):
            return Response({
                "message": "You don't the permissions for this action."
            })

        queryset = TaskSerializer(Task.objects.filter(
            user_id=user.get('id')), many=True).data
        return Response(queryset)
