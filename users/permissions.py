from rest_framework.permissions import BasePermission


class CreateOrIsAcontOner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == "POST":
            return True
        else:
            return request.user.is_authenticated and obj == request.user