from rest_framework.permissions import BasePermission


class EditCommentPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        user = self.context.get('request.user')
        return obj.user == user
        # if user in obj.user:
        #     return True
