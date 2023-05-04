from rest_framework.permissions import BasePermission
import ipdb


class IsAccountOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user_id == request.user.id
