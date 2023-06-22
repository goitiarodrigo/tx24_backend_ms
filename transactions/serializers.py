from rest_framework import serializers
from .models import Transactions
from django.db import models
from wallet.models import Wallet


class TransactionsSerializer(serializers.ModelSerializer):
    wallet = serializers.JSONField()

    class Meta:
        model = Transactions
        fields = '__all__'

    def validate(self, attrs):
        user = attrs.get('user')
        type_currency_purchased = attrs.get('type_currency_purchased')
        type_currency_used = attrs.get('type_currency_used')
        type_of_transaction = attrs.get('type_of_transaction')
        amount = attrs.get('amount')
        purchase_price = attrs.get('purchase_price')
        wallet = attrs.get('wallet')

        try:
            wallet_sent = Wallet.objects.filter(user=user, crypto_name=wallet['balance_spent']['coin']).first()
            if wallet_sent:
                wallet_sent.balance -= wallet['balance_spent']['quantity']
                wallet_sent.save()
            wallet_sent = Wallet.objects.filter(user=user, crypto_name=wallet['purchased_balance']['coin']).first()
            if wallet_sent:
                wallet_sent.balance += wallet['purchased_balance']['quantity']
                wallet_sent.save()
            else:
                 wallet_obj = Wallet(
                      user=user,
                      crypto_name=wallet['purchased_balance']['coin'],
                      balance=wallet['purchased_balance']['quantity']
                 )
                 wallet_obj.save()
            transaction = Transactions(
                user=user,
                type_currency_purchased=type_currency_purchased,
                type_currency_used=type_currency_used,
                type_of_transaction=type_of_transaction,
                amount=amount,
                purchase_price=purchase_price,
            )
            transaction.save()
            attrs['transaction']=transaction

        except Exception as e:
                raise serializers.ValidationError(e)
        
        return attrs

class GetTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = '__all__'