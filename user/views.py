from .models import User
from rest_framework import viewsets, permissions, response
from rest_framework_simplejwt.tokens import AccessToken
import jwt
from .serializers import UserLoginSerializer, UserRegisterSerializer
from django.conf import settings
from datetime import datetime, timedelta

secret_key = settings.SECRET_KEY

class UserLoginViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserLoginSerializer

    def login(self, request):
        try:
            serializer = UserLoginSerializer(data = request.data)
            serializer.is_valid(raise_exception = True)
            user = serializer.validated_data['user']

            payload = {
                "user_id": user.id,
                "username": user.username,
                "exp": datetime.utcnow() + timedelta(days=2)
            }
            token = jwt.encode(payload, secret_key, algorithm="HS256")
            response_data = {
                'access_token': token,
                'user': {
                        'email': user.email,
                        'username': user.username,
                        'id': user.id
                    }
            }
            return response.Response(response_data)

        except ValueError as error:
            return response.Response(str(error))
    

class UserRegisterViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserRegisterSerializer

    def register(self, request):
        try:
            serializer = UserRegisterSerializer(data = request.data)
            serializer.is_valid(raise_exception = True)
            try:
                user = serializer.validated_data['user']
                token = AccessToken.for_user(user)
                response_data = {
                    'access_token': str(token),
                    'user': {
                            'email': user.email,
                            'username': user.username,
                            'id': user.id
                        }
                    }
                return response.Response(response_data)
            except: serializer.ValueError('An error has occurred to create token')
        except ValueError as Error:
            return response.Response(str(Error)) 