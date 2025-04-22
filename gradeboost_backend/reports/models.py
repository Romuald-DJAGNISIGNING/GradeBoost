

from django.db import models
from users.models import User

class Report(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
        ('Dismissed', 'Dismissed')
    ]

    reporter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='submitted_reports')
    reported_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_reports')
    subject = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.subject} - {self.reporter.username} ➝ {self.reported_user.username}"
