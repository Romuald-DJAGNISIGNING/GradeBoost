from django.db import models
from django.conf import settings
from django.utils import timezone

SESSION_TYPES = (
    ('on_campus', 'On-Campus'),
    ('off_campus', 'Off-Campus'),
)

def assignment_submission_path(instance, filename):
    return f"assignments/{instance.student.username}_{filename}"

class Session(models.Model):
    tutor = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='tutor_custom_sessions', on_delete=models.CASCADE)
    student = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='student_custom_sessions', on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    session_type = models.CharField(max_length=15, choices=SESSION_TYPES)
    classroom = models.CharField(max_length=50, blank=True, null=True)
    location_link = models.URLField(blank=True, help_text="Paste Google Maps location if off-campus.")
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_approved = models.BooleanField(default=False)
    is_canceled = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.subject} | {self.tutor} -> {self.student} | {self.session_type}"

class AssignmentSubmission(models.Model):
    assignment = models.ForeignKey(
        'dashboard.Assignment',
        on_delete=models.CASCADE,
        related_name='dashboard_assignmentsubmissions'  # Add a unique related_name
    )
    student = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name='dashboard_assignmentsubmissions'  # Add a unique related_name
    )
    file = models.FileField(upload_to=assignment_submission_path)
    submitted_at = models.DateTimeField(auto_now_add=True)

    feedback = models.TextField(blank=True, null=True)
    grade = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    feedback_provided = models.BooleanField(default=False)
    graded = models.BooleanField(default=False)
    feedback_provided_at = models.DateTimeField(blank=True, null=True)
    graded_at = models.DateTimeField(blank=True, null=True)
