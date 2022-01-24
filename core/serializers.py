from rest_framework import serializers
from django.contrib.auth.models import User

# ? para mostrar el usuario
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
        # fields = ('__all__')


