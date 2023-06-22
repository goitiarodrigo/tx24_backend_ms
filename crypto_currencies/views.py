from .models import Crypto_Currency
from .serializers import UploadCrypto_CurrencySerializer, GetCrypto_CurrencySerializer
from rest_framework import viewsets, permissions, response, status
from utils.validate_token import validate_token

# Create your views here.
class CryptoViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Crypto_Currency.objects.all()
    serializer_class = GetCrypto_CurrencySerializer

    def get_coins(self, request):
        if validate_token(request.META.get('HTTP_AUTHORIZATION', '')):
            coins = Crypto_Currency.objects.all()
            serializer = self.get_serializer(data=coins, many=True)
            serializer.is_valid()
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return response.Response({'message': 'Access denied'}, status=status.HTTP_401_UNAUTHORIZED)


class UploadCrypto_CurrencyViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Crypto_Currency.objects.all()
    serializer_class = UploadCrypto_CurrencySerializer

    def upload_coins(self, request):
        if validate_token(request.META.get('HTTP_AUTHORIZATION', '')):
            for data in request.data:
                serializer = UploadCrypto_CurrencySerializer(data=data)
                serializer.is_valid(raise_exception=True)

            return response.Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return response.Response({'message': 'Access denied'}, status=status.HTTP_401_UNAUTHORIZED)