from django.db import models
from django.conf import settings  # Import settings for AUTH_USER_MODEL


def assignment_submission_path(instance, filename):
    return f"assignments/{instance.student.username}_{filename}"


class Assignment(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateTimeField()

    def __str__(self):
        return self.title


class AssignmentSubmission(models.Model):
    assignment = models.ForeignKey('dashboard.Assignment', on_delete=models.CASCADE)  # Use string reference
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Use AUTH_USER_MODEL for User
    file = models.FileField(upload_to=assignment_submission_path)
    submitted_at = models.DateTimeField(auto_now_add=True)

    feedback = models.TextField(blank=True, null=True)
    grade = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    feedback_provided = models.BooleanField(default=False)
    graded = models.BooleanField(default=False)
    feedback_provided_at = models.DateTimeField(blank=True, null=True)
    graded_at = models.DateTimeField(blank=True, null=True)
