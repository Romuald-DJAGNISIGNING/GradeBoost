from django.db import models
from users.models import User
from custom_sessions.models import Session

class StudentProgress(models.Model):
    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'student'},
        related_name='student_progress'  # Unique related_name for students
    )
    tutor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'tutor'},
        related_name='tutor_progress'  # Unique related_name for tutors
    )
    session = models.ForeignKey(Session, on_delete=models.SET_NULL, null=True, blank=True)
    subject = models.CharField(max_length=100)
    grade = models.FloatField()
    feedback = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.student.username} - {self.subject} ({self.grade})"
