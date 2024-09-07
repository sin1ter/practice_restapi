from accounts.models import *
from rest_framework import serializers

from django.contrib.auth.password_validation import validate_password

class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)

    class Meta:
        model = MyUser
        fields = ['email', 'username', 'profile', 'password', 'password2']
        extra_kwargs = {'password': {'write_only': True}}

    def save(self):

        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'error': 'Passwords must match.'})
        
        if MyUser.objects.filter(username=self.validated_data['username']).exists():
            raise serializers.ValidationError({'error': "Username already exists."})
        
        if MyUser.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error': 'Email already exists.'})
        
        account = MyUser(email=self.validated_data['email'], 
                       username=self.validated_data['username'])
        account.set_password(password)
        account.save()

        return account
    
class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['username', 'email'] 

class ChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({'error': 'Passwords must match.'})
        return data

    def save(self, **kwargs):
        user = self.instance
        user.set_password(self.validated_data['password'])
        user.save()
        return user
        
        



