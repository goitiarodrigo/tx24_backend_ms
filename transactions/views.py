from .models import Transactions
from .serializers import TransactionsSerializer, GetTransactionSerializer
from rest_framework import viewsets, permissions, response, status
from utils.validate_token import validate_token

# Create your views here.
class TransactionsViewSet(viewsets.ModelViewSet):
    queryset = Transactions.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TransactionsSerializer

    def post_transaction(self, request):
        try:
            if validate_token(request.META.get('HTTP_AUTHORIZATION', '')):
                serializer = TransactionsSerializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                return response.Response({'data': serializer.data, 'success': True}, status = status.HTTP_200_OK)
            else :
                return response.Response({'message': 'Access denied'}, status=status.HTTP_401_UNAUTHORIZED)
        except ValueError as Error:
            return response.Response(str(Error))


class GetTransactionsViewSet(viewsets.ModelViewSet):
    queryset = Transactions.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TransactionsSerializer

    def get_transactions(self, request):
        try:
            if validate_token(request.META.get('HTTP_AUTHORIZATION', '')):
                user_id = request.query_params.get('id')
                if user_id:
                    transaction = Transactions.objects.filter(user_id=user_id)
                    if transaction:
                        serializer = GetTransactionSerializer(transaction, many=True)
                        return response.Response({'data': serializer.data, 'success': True}, status=status.HTTP_200_OK)
                    else:
                        return response.Response({'message': 'Transaction not found'}, status=status.HTTP_404_NOT_FOUND)
                else:
                    return response.Response({'message': 'Parameter "id" is missing'}, status=status.HTTP_400_BAD_REQUEST)
            else :
                return response.Response({'message': 'Access denied'}, status=status.HTTP_401_UNAUTHORIZED)
        except ValueError as Error:
            return response.Response(str(Error))