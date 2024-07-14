from rest_framework.permissions import BasePermission

class AdminPermission(BasePermission):
    def has_permission(self, request, view):
        print(request.user.user_type.name)
        if request.user.user_type.name=="Admin User":
            return True
        else:
            return False
        
class NormalUserPermission(BasePermission):
    def has_permission(self, request, view):
    
        if request.user.user_type.name=="Normal User":
            return True
        else:
            return False

