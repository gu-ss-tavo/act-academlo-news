from rest_framework import permissions

class IsUserInFeedbackOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # ? verdadero sí no son métodos riesgosos
        if request.method in permissions.SAFE_METHODS:
            return True

        elif request.method == 'DELETE':
            # ? verdadero sí el usuario creó el post y el metodo es DELETE
            if request.user == obj.post.user:
                return True

        # ? verdadero sí el usuario creó el comentario
        return obj.user == request.user
