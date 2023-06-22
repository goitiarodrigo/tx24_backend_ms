from django.contrib import admin
from django.urls import path, include
from user.views import UserRegisterViewSet, UserLoginViewSet
from crypto_currencies.views import CryptoViewSet, UploadCrypto_CurrencyViewSet
from transactions.views import TransactionsViewSet, GetTransactionsViewSet
from wallet.views import WalletViewSet, AccreditViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/upload_coins/', UploadCrypto_CurrencyViewSet.as_view({'put': 'upload_coins'}), name = 'upload_coins'),
    path('api/login/', UserLoginViewSet.as_view({'post': 'login'}), name = 'login'),
    path('api/register/', UserRegisterViewSet.as_view({'post': 'register'}), name = 'register'),
    path('api/post_transaction/', TransactionsViewSet.as_view({'post': 'post_transaction'}), name = 'post_transaction'),
    path('api/accredit_balance/', AccreditViewSet.as_view({'post': 'accredit_balance'}), name = 'accredit_balance'),
    path('api/get_transactions/', GetTransactionsViewSet.as_view({'get': 'get_transactions'}), name = 'get_transactions'),
    path('api/get_coins/', CryptoViewSet.as_view({'get': 'get_coins'}), name = 'get_coins'),
    path('api/get_coin_wallet/', WalletViewSet.as_view({'get': 'get_coin_wallet'}), name = 'get_coin_wallet')
]
