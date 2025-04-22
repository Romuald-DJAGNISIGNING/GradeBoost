from rest_framework import generics, permissions
from django.shortcuts import render
from .models import Review
from .serializers import ReviewSerializer
from users.models import User

class ReviewCreateView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        session = self.request.data.get('session')
        tutor = self.request.data.get('tutor')
        serializer.save(student=self.request.user, session_id=session, tutor_id=tutor)

class TutorReviewListView(generics.ListAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        tutor_id = self.kwargs['tutor_id']
        return Review.objects.filter(tutor_id=tutor_id).order_by('-created_at')

def tutor_profile(request, tutor_id):
    tutor = User.objects.get(pk=tutor_id)
    avg_rating = Review.get_tutor_average_rating(tutor)
    return render(request, 'tutor_profile.html', {'tutor': tutor, 'avg_rating': avg_rating})
