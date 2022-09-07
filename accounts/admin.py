from django.contrib import admin

from accounts.models import User


class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'is_active')
    list_filter = ('date_joined', 'is_active', 'is_staff')


admin.site.register(User, AccountAdmin)
