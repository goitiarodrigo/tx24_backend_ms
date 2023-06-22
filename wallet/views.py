from rest_framework import viewsets, permissions, response, status
from .models import Wallet
from utils.validate_token import validate_token
from .serializer import WalletSerializer, AccreditSerializer

# Create your views here.
class WalletViewSet(viewsets.ModelViewSet):
    queryset = Wallet.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = WalletSerializer

    def get_coin_wallet(self, request):
        try:
            if validate_token(request.META.get('HTTP_AUTHORIZATION', '')):
                user_id = request.query_params.get('id')
                if user_id:
                    wallet = Wallet.objects.filter(user_id=user_id)
                    if wallet:
                        serializer = WalletSerializer(wallet, many=True)
                        return response.Response({'data': serializer.data, 'success': True}, status=status.HTTP_200_OK)
                    else:
                        return response.Response({'data': [], 'success': True}, status=status.HTTP_200_OK)
                else:
                    return response.Response({'message': 'Parameter "id" is missing'}, status=status.HTTP_400_BAD_REQUEST)
            else :
                return response.Response({'message': 'Access denied'}, status=status.HTTP_401_UNAUTHORIZED)
        except ValueError as Error:
            return response.Response(str(Error))


class AccreditViewSet(viewsets.ModelViewSet):
    queryset = Wallet.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = WalletSerializer

    def accredit_balance(self, request):
        try:
            if validate_token(request.META.get('HTTP_AUTHORIZATION', '')):
                serializer = AccreditSerializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                return response.Response({'data': serializer.data, 'success': True}, status = status.HTTP_200_OK)
            else :
                return response.Response({'message': 'Access denied'}, status=status.HTTP_401_UNAUTHORIZED)
        except ValueError as Error:
            return response.Response(str(Error))