from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator
from allauth.socialaccount.models import SocialAccount  # Import SocialAccount for Google profile picture

from .utils import get_default_profile_pic

GENDER_CHOICES = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other'),
)

USER_ROLES = (
    ('student', 'Student'),
    ('tutor', 'Tutor'),
    ('admin', 'Admin'),
)

RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]

def get_default_profile_pic():
    return 'profile_pics/default_profile_pic.png'


class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True, null=True)
    role = models.CharField(
        max_length=10,
        choices=USER_ROLES,
        blank=True,
        null=True,
        default='student'  # Default role is 'student'
    )

    profile_pic = models.ImageField(
        upload_to='profile_pics/',
        blank=True,
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])],
        default=get_default_profile_pic
    )

    id_card = models.ImageField(
        upload_to='id_cards/',
        validators=[FileExtensionValidator(['jpg', 'jpeg', 'png'])],
        help_text="Upload a valid official ID with your photo and full name.",
    )

    # Tutor-specific
    transcript = models.FileField(
        upload_to='transcripts/',
        validators=[FileExtensionValidator(['pdf'])],
        blank=True,
        null=True,
        help_text="Upload the tutor's transcript for evaluation."
    )
    subjects = models.TextField(blank=True, help_text="Comma-separated list of subjects (e.g., Math, Physics)")
    default_rating = models.IntegerField(
        choices=RATING_CHOICES,
        default=3,  # Default rating for tutors
        help_text="Default rating assigned by the admin based on the transcript."
    )

    # Student-specific
    timetable = models.FileField(
        upload_to='timetables/',
        validators=[FileExtensionValidator(['pdf'])],
        blank=True,
        null=True
    )
    
    is_off_campus = models.BooleanField(default=False, help_text="Check if tutoring is off-campus.")

    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        blank=True,
        null=True,
        help_text="Latitude for off-campus location"
    )

    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        blank=True,
        null=True,
        help_text="Longitude for off-campus location"
    )

    is_suspended = models.BooleanField(default=False)
    warning_count = models.IntegerField(default=0)

    received_reviews = models.ManyToManyField(
        'reviews.Review',
        related_name='reviewed_user',
        blank=True
    )

    REQUIRED_FIELDS = ['email', 'phone', 'first_name', 'last_name']

    def __str__(self):
        return f"{self.username} ({self.role})"

    def save(self, *args, **kwargs):
        if not self.pk:
            if self.role not in ['student', 'tutor']:
                self.role = 'student'
        else:
            if not self.is_superuser:
                original_user = User.objects.get(pk=self.pk)
                if original_user.role == 'admin' and self.role != 'admin':
                    raise ValueError("Only an admin can demote another admin.")
                if self.role == 'admin':
                    raise ValueError("Only an admin can promote a user to admin.")
        super().save(*args, **kwargs)

    def save_google_picture(self):
        try:
            social_account = SocialAccount.objects.get(user=self, provider='google')
            profile_picture_url = social_account.extra_data.get('picture')
            if profile_picture_url:
                import requests
                from django.core.files.base import ContentFile

                response = requests.get(profile_picture_url)
                if response.status_code == 200:
                    self.profile_pic.save(
                        f"{self.username}_google_profile.jpg",
                        ContentFile(response.content),
                        save=False
                    )
        except SocialAccount.DoesNotExist:
            pass
