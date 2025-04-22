

from rest_framework import generics, permissions
from .models import Payment, PaymentSettings
from .serializers import PaymentSerializer, PaymentSettingsSerializer

class PaymentListCreateView(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]

class PaymentDetailView(generics.RetrieveAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]

class PaymentSettingsView(generics.RetrieveUpdateAPIView):
    queryset = PaymentSettings.objects.all()
    serializer_class = PaymentSettingsSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_object(self):
        return PaymentSettings.objects.first()
