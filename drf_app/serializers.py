from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.hashers import make_password

class UserSerializers(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        user = User.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data['password'])
        return super().update(instance, validated_data)
    
class UpdateUser(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','email']

    def update(self, instance, validated_data):
        instance.username=validated_data.get('username',instance.username)
        instance.email=validated_data.get('email',instance.email)
        instance.save()
        return instance

class LoginSerializers(serializers.ModelSerializer):
    username=serializers.CharField()
    password=serializers.CharField(write_only=True)

    class Meta:
        model=User
        fields=['username','password']

    def validate(self, data):
        username=data.get('username','')
        password=data.get('password','')
        if username and password:
            user=User.objects.filter(username=username).first()
            if user is None:
                raise AuthenticationFailed('User not found')
            if not user.check_password(password):
                raise AuthenticationFailed('Incorrect password')
        else:
            raise AuthenticationFailed('Username and password required')
        
        return user