from rest_framework.permissions import BasePermission

class IsAccountOwnerOrPostOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user_id == request.user.id
