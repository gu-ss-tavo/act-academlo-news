from django.contrib.auth.models import AnonymousUser
from rest_framework import status, viewsets, mixins
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from feedback.models import Feedback
from feedback.serializers import FeedbackSerializer

from .models import CustomUser
from .serializers import CustomUserSerializer

# ? vista al registrar un usuario
class RegisterUserViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    serializer_class = CustomUserSerializer
    model = CustomUser

# ? vista para mostrar el usuario actual
class UserViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def get_queryset(self):
        user = super().get_queryset().filter(id=self.request.user.id)
        return user

    # ? ACCIÓN que muestra todos los comentarios que contiene el usuario
    @action(detail=False, methods=['GET'])
    def my_comments(self, request):
        user = request.user
        comments = Feedback.objects.filter(user__id=user.id)
        serialized = FeedbackSerializer(comments, many=True)

        if not comments:
            return Response(status=status.HTTP_404_NOT_FOUND,
                            data={
                                "message":"You haven't commented on anything"
                            })
        return Response(status=status.HTTP_200_OK, data=serialized.data)
