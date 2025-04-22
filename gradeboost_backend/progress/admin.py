from django.contrib import admin
from .models import StudentProgress

@admin.register(StudentProgress)
class StudentProgressAdmin(admin.ModelAdmin):
    list_display = ('student', 'tutor', 'subject', 'grade', 'created_at')
    search_fields = ('student__username', 'subject')