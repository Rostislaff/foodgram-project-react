from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

User = get_user_model()


# @admin.register(User)
# # class UserAdmin(admin.ModelAdmin):
# class UserAdmin(BaseUserAdmin):
#     list_display = (
#         'id', 'username', 'email',
#         'first_name', 'last_name', 'date_joined',
#     )
#     search_fields = ('email', 'username', 'first_name', 'last_name')
#     list_filter = ('date_joined', 'email', 'first_name')
#     empty_value_display = '-пусто-'

#     def get_readonly_fields(self, request, obj=None):
#         readonly_fields = list(self.readonly_fields) + ['last_login']
#         return readonly_fields

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = (
        'id', 'username', 'password', 'email', 'first_name', 'last_name',
    )
    list_editable = ('password',)
    fields = (
        'email', 'password', 'username', 'first_name', 'last_name',
        'is_active', 'is_staff', ('last_login', 'date_joined')
    )
    fieldsets = []
    list_filter = ('email', 'username')
    readonly_fields = ('last_login', 'date_joined',)

