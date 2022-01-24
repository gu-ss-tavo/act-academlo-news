from rest_framework import serializers

from .models import Feedback
from core.serializers import UserSerializer
from post.serilizers import PostSerializer

# ? para mostrar todo los comentarios
class FeedbackSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    post = PostSerializer(read_only=True)
    class Meta:
        model = Feedback
        fields = ('__all__')

# ? para crear un nuevo comentario
class FeedbackCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Feedback
        fields = ('__all__')
