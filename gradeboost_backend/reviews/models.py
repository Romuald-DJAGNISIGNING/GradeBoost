from django.db import models
from django.db.models import Avg
from users.models import User
from custom_sessions.models import Session  # Import the Session model

RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]


class Review(models.Model):
    session = models.ForeignKey(
        Session,  # Link to the Session model
        on_delete=models.CASCADE,
        related_name='reviews'  # Add a unique related_name
    )
    tutor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='tutor_reviews'  # Add a unique related_name
    )
    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='student_reviews'  # Add a unique related_name
    )
    rating = models.IntegerField(choices=RATING_CHOICES)
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.tutor.username} by {self.student.username}"

    @staticmethod
    def get_tutor_average_rating(tutor):
        """
        Calculate the average rating for a tutor.
        """
        reviews = Review.objects.filter(tutor=tutor)
        if reviews.exists():
            return reviews.aggregate(Avg('rating'))['rating__avg']
        return 0  # No reviews yet
