from django.contrib import admin

from .models import Dday
from .forms import DdayCreationForm

# Register your models here.
@admin.register(Dday)
class DdayAdmin(admin.ModelAdmin):
    form = DdayCreationForm
    list_display = ("title", "start_date", "end_date", "created_at")

    fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ("title", "start_date", "end_date", "created_at")
        }),
    )