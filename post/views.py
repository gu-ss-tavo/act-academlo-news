from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Post
from .serilizers import PostSerializer, PostCreateSerializer

# Create your views here.
class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return PostCreateSerializer
        return PostSerializer
