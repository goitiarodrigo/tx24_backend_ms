from rest_framework import serializers
from django.contrib.auth.hashers import make_password, check_password
from .models import User

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = User.objects.filter(email = email).first()
            if user is None :
                raise serializers.ValidationError('Email does not exist')

            if user and check_password(password, user.password) :
                attrs['user'] = user
            else:
                raise serializers.ValidationError('Email or password incorrect')
        else:
            raise serializers.ValidationError('Should be send email and password')

        return attrs

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}
    
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        username = attrs.get('username')

        if email and password and username:
            user = User.objects.filter(email = email).first()
            if user != None:
                raise serializers.ValidationError('A user already exists')
            else:
                try:
                    hashed_password = make_password(password)
                    user = User(username = username, email = email, password = hashed_password)
                    user.save()
                    attrs['user'] = user
                except: serializers.ValidationError('An error has ocurred to save new user')
        else:
            raise serializers.ValidationError('All fields should be completed')
        
        return attrs