from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer, UserLoginSerializer
from django.contrib.auth.hashers import check_password


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AuthenticationView(APIView):
    def post(self, request):
        # request.data = es la informacion que recibmos del cliente
        user_request = UserLoginSerializer(data=request.data)

        if not user_request.is_valid():
            return Response({"message:": "Email y/o password incorrectos"}, status=401)

        # buscar el usuario por correo
        user = User.objects.get(email=user_request.data['email'])

        if not user:
            return Response({"message:": "Email y/o password incorrectos"}, status=401)

        # comparar que el password sea correcto
        user_serializer = UserSerializer(user).data
        if not check_password(user_request.data['password'], user_serializer.get('password')):
            return Response({"message:": "Email y/o password incorrectos"}, status=401)

        return Response({"message": user_serializer})
