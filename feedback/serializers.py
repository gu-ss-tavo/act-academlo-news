from django.contrib.auth.models import AnonymousUser
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Feedback
from user.serializers import CustomUserSerializer
from post.serilizers import PostSerializer

# ? para mostrar todo los comentarios
class FeedbackSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)
    class Meta:
        model = Feedback
        fields = ('__all__')

# ? para crear un nuevo comentario
class FeedbackCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def create(self, validated_data):
        user = validated_data.get('user')
        body = validated_data.get('body')

        if isinstance(user, AnonymousUser):
            raise ValidationError(('log in first'), code='invalid')

        feedback = Feedback(user=user, body=body)
        feedback.save()
        return feedback

    class Meta:
        model = Feedback
        fields = ('__all__')
