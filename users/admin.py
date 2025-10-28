from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import CustomUser


# Register your models here.
class CustomUserAdmin(UserAdmin):
    # Добавляем groups в fieldsets
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    # Для лучшего отображения ManyToMany полей
    filter_horizontal = ('groups', 'user_permissions')


# Перерегистрируем с новой конфигурацией
# admin.site.unregister(CustomUser)
admin.site.register(CustomUser, CustomUserAdmin)
