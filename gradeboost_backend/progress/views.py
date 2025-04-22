

from rest_framework import generics, permissions
from .models import StudentProgress
from .serializers import StudentProgressSerializer

class AddProgressView(generics.CreateAPIView):
    serializer_class = StudentProgressSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(tutor=self.request.user)

class StudentProgressListView(generics.ListAPIView):
    serializer_class = StudentProgressSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'student':
            return StudentProgress.objects.filter(student=user)
        elif user.role == 'tutor':
            return StudentProgress.objects.filter(tutor=user)
        return StudentProgress.objects.none()
