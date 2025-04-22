

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from users.models import User
from custom_sessions.models import Session
from payments.models import Payment
from reviews.models import Review
from reports.models import Report
from django.db.models import Avg

class AdminDashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if not request.user.is_superuser:
            return Response({"detail": "Not authorized"}, status=403)

        return Response({
            "total_users": User.objects.count(),
            "total_students": User.objects.filter(role='student').count(),
            "total_tutors": User.objects.filter(role='tutor').count(),
            "total_custom_sessions": Session.objects.count(),
            "total_payments": Payment.objects.count(),
            "pending_reports": Report.objects.filter(status='Pending').count(),
            "recent_reviews": list(Review.objects.order_by('-created_at')[:5].values('student__username', 'tutor__username', 'rating', 'feedback'))
        })

class TutorDashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.role != 'tutor':
            return Response({"detail": "Not authorized"}, status=403)

        return Response({
            "assigned_custom_sessions": Session.objects.filter(tutor=request.user).count(),
            "average_rating": Review.objects.filter(tutor=request.user).aggregate(Avg('rating'))['rating__avg'] or 0,
            "homework_submitted": request.user.received_homeworks.count(),
            "total_earnings": Payment.objects.filter(tutor=request.user, is_paid=True).aggregate(total=models.Sum('amount'))['total'] or 0
        })

class StudentDashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.role != 'student':
            return Response({"detail": "Not authorized"}, status=403)

        return Response({
            "booked_custom_sessions": Session.objects.filter(student=request.user).count(),
            "reviews_given": Review.objects.filter(student=request.user).count(),
            "progress_chart": {
                "grades": list(request.user.received_grades.values('score', 'comment', 'created_at')),
            },
            "pending_homework": request.user.submitted_homeworks.filter(is_submitted=False).count()
        })
