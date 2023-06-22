from rest_framework import serializers
from .models import Crypto_Currency

class UploadCrypto_CurrencySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=False)

    class Meta:
        model = Crypto_Currency
        fields = '__all__'
    
    def validate(self, attrs):
        required_fields = ['name', 'abbreviation', 'image', 'old_price', 'current_price', 'previous_day_price', 'id']
        data = {field: attrs.get(field) for field in required_fields}

        if all(value is not None for value in data.values()):
            try:
                crypto = Crypto_Currency.objects.get(id = data['id'])
                crypto.name = data['name']
                crypto.abbreviation = data['abbreviation']
                crypto.image = data['image']
                crypto.old_price = data['old_price']
                crypto.current_price = data['current_price']
                crypto.previous_day_price = data['previous_day_price']
                crypto.previous_day_price = data['previous_day_price']
                crypto.save()
                
                self.instance = crypto
            except: 
                serializers.ValidationError('An error has occurred to update data')
        else:
            serializers.ValidationError('All fields are required')
        return attrs

class GetCrypto_CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Crypto_Currency
        fields = '__all__'