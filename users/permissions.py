from rest_framework.permissions import BasePermission


class CreateOrIsAccountOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == "GET":
            return True
        else:
            return request.user.is_authenticated and obj == request.user
