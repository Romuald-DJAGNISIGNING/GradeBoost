from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['session', 'student', 'tutor', 'rating', 'created_at', 'tutor_stars']
    list_filter = ['rating', 'created_at']
    search_fields = ['student__username', 'tutor__username', 'session__id']

    def tutor_stars(self, obj):
        return Review.get_tutor_average_rating(obj.tutor)

    tutor_stars.short_description = 'Tutor Rating'
