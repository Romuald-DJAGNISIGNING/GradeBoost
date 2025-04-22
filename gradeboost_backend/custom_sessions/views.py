

from rest_framework import generics, permissions
from .models import Session
from .serializers import custom_sessionserializer
from django.utils import timezone

class SessionListCreateView(generics.ListCreateAPIView):
    queryset = Session.objects.all()
    serializer_class = custom_sessionserializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)

class SessionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Session.objects.all()
    serializer_class = custom_sessionserializer
    permission_classes = [permissions.IsAuthenticated]
