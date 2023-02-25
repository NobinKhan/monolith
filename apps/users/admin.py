from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as UA

from apps.users.models import User



@admin.register(User)
class UserAdmin(UA):
    ordering = ('-id', )
    # inlines = (EmailInline,)
    search_fields = ("primary_email", "username")
    list_filter = ("is_active", "is_staff", "is_superuser")
    list_display = ("username", "primary_email", "is_staff", "is_superuser", "is_active", "created_at", "updated_at")
    fieldsets = (

        ('Login Info', {
            'classes': ('wide',),
            'fields': ('username','primary_email', 'is_active', 'is_staff',)
        }),
        # ('Personal Info', {
        #     'classes': ('wide',),
        #     'fields': ('email', 'firebase_device_id')
        # }),
        ('Group Permissions (User Role)', {
            'classes': ('collapse',),
            'fields': ('groups', 'user_permissions', )
        }),
        ('Timestamps', {
            'classes': ('collapse', ),
            'fields': (("created_at", "updated_at"),)
        }),
    )
    
    add_fieldsets = (
        ('Login Info', {
            'classes': ('wide',),
            'fields': ('username', 'primary_email', 'password1', 'password2', 'is_active', 'is_staff'),
        }),
        
        ('Group Permissions (User Role)', {
            'classes': ('collapse',),
            'fields': ('groups', 'user_permissions', )
        }),
        # ('Important Dates', {
        #     'classes': ('collapse', ),
        #     'fields': (("created_at", "updated_at"),)
        # }),
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )


