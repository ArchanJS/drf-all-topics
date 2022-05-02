from rest_framework.permissions import BasePermission

class PostPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method=='GET' or request.method=='POST':
            return True
        return False