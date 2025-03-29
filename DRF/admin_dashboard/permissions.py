from rest_framework.permissions import BasePermission

class IsSuperUser(BasePermission):
    """
    Custom permission to allow only superusers (admins) to access endpoints.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.is_superuser
