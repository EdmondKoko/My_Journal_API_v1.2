from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """Пользователь может просматривать любые записи, но может изменять или удалять только свои записи."""
    
    def has_permission(self, request, view):
        """Проверка наличия разрешения на выполнение действия."""
        if (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated):
            return True

    def has_object_permission(self, request, view, obj):
        """Проверка наличия разрешения на выполнение действия над объектом."""
        if obj.author:
            author = obj.author
        else:
            author = obj.user
        if (request.method in permissions.SAFE_METHODS
                or author == request.user):
            return True
