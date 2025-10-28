from django.core.exceptions import PermissionDenied


class OwnerRequiredMixin:
    """Миксин для проверки, что пользователь является владельцем объекта"""

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()

        # Проверяем, является ли пользователь владельцем
        if obj.owner != request.user:
            raise PermissionDenied("Вы не являетесь владельцем этого товара")

        return super().dispatch(request, *args, **kwargs)


class OwnerOrModeratorRequiredMixin:
    """Миксин для проверки, что пользователь является владельцем ИЛИ модератором"""

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()

        # Проверяем, является ли пользователь владельцем ИЛИ имеет право на удаление
        if obj.owner != request.user and not request.user.has_perm('catalog.can_delete_product'):
            raise PermissionDenied("Вы не являетесь владельцем этого товара и не имеете прав модератора")

        return super().dispatch(request, *args, **kwargs)