from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""

    def has_object_permission(self, request, view, obj): #this will call everytime a request is made to the API \\ return true / false
        """Check user is trying to edit their own profile"""
        print("Fuck I'm here 1")
        if request in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id
