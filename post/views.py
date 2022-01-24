from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .permissions import IsUserInPostOrReadOnly
from .models import Post
from .serilizers import CommentsOnPostSerializer, PostSerializer, PostCreateSerializer

from feedback.models import Feedback

# ? vista completa de los posts
class PostViewSet(ModelViewSet):
    permission_classes = (IsUserInPostOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # ? vista por métodos
    def get_serializer_class(self):
        if self.action == 'create':
            return PostCreateSerializer
        return PostSerializer

    # ? ACCIÓN que muestra todos los comentarios que contiene el post
    @action(detail=True, methods=['GET'])
    def comments(self, request, pk=None):
        post = self.get_object()
        comments = Feedback.objects.filter(post__id=post.id)
        serialized = CommentsOnPostSerializer(comments, many=True)

        if not comments:
            return Response(status=status.HTTP_404_NOT_FOUND,
                            data={
                                "message":"This post has no comments"
                            })
        return Response(status=status.HTTP_200_OK, data=serialized.data)
