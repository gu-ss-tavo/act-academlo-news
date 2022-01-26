from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import CustomUser

# ? para crear y mostrar el usuario
class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        email = validated_data.get('email')
        password = validated_data.get('password')
        user = CustomUser(email=email, password=make_password(password))
        user.save()
        return user

    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'password')
