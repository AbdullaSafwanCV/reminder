from django.contrib import admin

from .models import Reminder

# Register your models here.
@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'is_completed', 'created_at')
    search_fields = ('title', 'description')
