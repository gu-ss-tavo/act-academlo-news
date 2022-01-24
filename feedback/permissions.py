from rest_framework import permissions

class IsUserInFeedbackOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.method == 'DELETE':
            if request.user == obj.post.user:
                return True

        return obj.user == request.user
