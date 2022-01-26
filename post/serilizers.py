from django.contrib.auth.models import AnonymousUser
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Post
from user.serializers import CustomUserSerializer
from feedback.models import Feedback

# ? para mostrar todo los artículos
class PostSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)
    class Meta:
        model = Post
        fields = ('__all__')

# ? para crear un nuevo artículo
class PostCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def create(self, validated_data):
        user = validated_data.get('user')
        title = validated_data.get('title')
        body = validated_data.get('body')

        if isinstance(user, AnonymousUser):
            raise ValidationError(('log in first'), code='invalid')

        post = Post(user=user, title=title, body=body)
        post.save()
        return post

    class Meta:
        model = Post
        fields = ('__all__')

# ? para mostrar los comentarios del post
class CommentsOnPostSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)
    class Meta:
        model = Feedback
        fields = ('id', 'user', 'body')
