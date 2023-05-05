from rest_framework.permissions import BasePermission


class IsFollowerToDelete(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.mothod == "Delete":
            return obj.follower == request.user