from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        user = request.user

        return obj.owner.id == user.id
