from rest_framework import permissions

class IsUserInPostOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # ? verdarero sí no son métodos riesgosos
        if request.method in permissions.SAFE_METHODS:
            return True

        # ? verdadero sí el usuario creó el post
        # ? verdadero sí el usuario es admin
        return obj.user == request.user or request.user.is_superuser
