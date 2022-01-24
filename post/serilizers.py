from rest_framework import serializers

from .models import Post
from core.serializers import UserSerializer
from feedback.models import Feedback

# ? para mostrar todo los artículos
class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Post
        fields = ('__all__')

# ? para crear un nuevo artículo
class PostCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Post
        fields = ('__all__')

# ? para mostrar los comentarios del post
class CommentsOnPostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Feedback
        fields = ('id', 'user', 'body')
