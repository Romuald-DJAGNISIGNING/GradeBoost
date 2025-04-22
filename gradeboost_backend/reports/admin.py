from django.contrib import admin
from .models import Report

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('reporter', 'reported_user', 'subject', 'status', 'created_at')
    list_filter = ('status', 'created_at')