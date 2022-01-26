from rest_framework.routers import DefaultRouter

from user.views import RegisterUserViewSet, UserViewSet
from post.views import PostViewSet
from feedback.views import FeedbackViewSet


router = DefaultRouter()

router.register('v1/core/user', UserViewSet, basename='user')
router.register('v1/core/register', RegisterUserViewSet, basename='register')
router.register('v1/posts', PostViewSet, basename='posts')
router.register('v1/feedbacks', FeedbackViewSet, basename='feedbacks')
