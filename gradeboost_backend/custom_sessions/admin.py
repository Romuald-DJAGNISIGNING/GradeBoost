

from django.contrib import admin
from .models import Session

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ['subject', 'tutor', 'student', 'start_time', 'session_type', 'is_approved', 'is_canceled']
    list_filter = ['session_type', 'is_approved', 'is_canceled']
    search_fields = ['tutor__username', 'student__username', 'subject']
