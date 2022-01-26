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
