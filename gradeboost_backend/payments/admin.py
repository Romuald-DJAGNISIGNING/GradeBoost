

from django.contrib import admin
from .models import Payment, PaymentSettings

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['session', 'student', 'tutor', 'amount', 'method', 'status', 'created_at']
    list_filter = ['method', 'status']
    search_fields = ['student__username', 'tutor__username', 'transaction_id']

@admin.register(PaymentSettings)
class PaymentSettingsAdmin(admin.ModelAdmin):
    list_display = ['session_rate', 'off_campus_extra_fee']
