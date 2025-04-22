

from rest_framework import generics, permissions
from .models import Message
from .serializers import MessageSerializer

class SendMessageView(generics.CreateAPIView):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)

class MessageListView(generics.ListAPIView):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        contact_id = self.kwargs['contact_id']
        return Message.objects.filter(
            sender__id__in=[user.id, contact_id],
            receiver__id__in=[user.id, contact_id]
        ).order_by('timestamp')
