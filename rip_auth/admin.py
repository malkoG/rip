from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from .forms import RipUserCreationForm
from .models import RipUser

@admin.register(RipUser)
class RipUserAdmin(UserAdmin):
    form = RipUserCreationForm
    list_display = ("email", "real_name", "is_staff", "is_active")
    list_filter = ["is_staff", "is_active"]

    fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ("email", "username", "real_name", "password1", "password2")
        }),
    )