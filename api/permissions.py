from rest_framework import permissions

class IsOwnerOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        print(obj.user, request.user)
        return obj.user == request.user