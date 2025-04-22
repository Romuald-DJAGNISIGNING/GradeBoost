

from django.db import models
from django.conf import settings
from custom_sessions.models import Session

PAYMENT_METHODS = (
    ('orange_money', 'Orange Money'),
    ('mtn_money', 'MTN Mobile Money'),
)

TRANSACTION_STATUS = (
    ('pending', 'Pending'),
    ('success', 'Success'),
    ('failed', 'Failed'),
)

class PaymentSettings(models.Model):
    session_rate = models.DecimalField(max_digits=8, decimal_places=2, default=5000)
    off_campus_extra_fee = models.DecimalField(max_digits=8, decimal_places=2, default=2000)

    def __str__(self):
        return f"Session: {self.session_rate}, Off-Campus: {self.off_campus_extra_fee}"

class Payment(models.Model):
    session = models.OneToOneField(Session, on_delete=models.CASCADE)
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='student_payments')
    tutor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tutor_earnings')
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    method = models.CharField(max_length=20, choices=PAYMENT_METHODS)
    transaction_id = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=TRANSACTION_STATUS, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} → {self.tutor} | {self.amount} | {self.method} | {self.status}"
