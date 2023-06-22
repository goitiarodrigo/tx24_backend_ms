from rest_framework import serializers
from .models import Wallet

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = '__all__'

    def validate(self, attrs):
        return attrs
    
class AccreditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = '__all__'
    
    def validate(self, attrs):
        user = attrs.get('user')
        crypto_name = attrs.get('crypto_name')
        balance = attrs.get('balance')

        wallet_obj = Wallet(
                    user=user,
                    crypto_name=crypto_name,
                    balance=balance
                )
        wallet_obj.save()

        return attrs
