from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .permissions import IsUserInFeedbackOrReadOnly
from .models import Feedback
from .serializers import FeedbackSerializer, FeedbackCreateSerializer

# ? vista completa de los comentarios
class FeedbackViewSet(ModelViewSet):
    permission_classes = (IsUserInFeedbackOrReadOnly,)
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

    # ? vista por métodos
    def get_serializer_class(self):
        if self.action == 'create':
            return FeedbackCreateSerializer
        return FeedbackSerializer

    # ? ACCIÓN que muestra todos tus comentarios
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

