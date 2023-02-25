from django.contrib import admin

from apps.emails.models import Email

# Register your models here.
# class EmailInline(admin.TabularInline):
#     model = Email
#     fields = ("email",)
#     extra = 1

@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = ("email", "role", "created_at", "updated_at")
