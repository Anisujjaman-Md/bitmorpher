from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, RequestLog

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('user_type', 'authentication_token')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('user_type',)}),
    )
    list_display = ('username', 'email', 'user_type', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email')
    ordering = ('username',)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.set_password(form.cleaned_data['password1'])
        super().save_model(request, obj, form, change)

admin.site.register(CustomUser, CustomUserAdmin)

class RequestLogAdmin(admin.ModelAdmin):
    list_display = ('username', 'timestamp', 'path')
    search_fields = ('username', 'path')
    list_filter = ('timestamp',)
    ordering = ('-timestamp',)

admin.site.register(RequestLog, RequestLogAdmin)