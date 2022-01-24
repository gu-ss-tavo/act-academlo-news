from django.db import models

from django.contrib.auth.models import User
from post.models import Post

# Create your models here.
class Feedback(models.Model):
    post = models.ForeignKey(Post, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.user} -> {self.body}'
