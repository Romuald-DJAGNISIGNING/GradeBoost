

from django.urls import path
from .views import PaymentListCreateView, PaymentDetailView, PaymentSettingsView

urlpatterns = [
    path('', PaymentListCreateView.as_view(), name='payment-list'),
    path('<int:pk>/', PaymentDetailView.as_view(), name='payment-detail'),
    path('settings/', PaymentSettingsView.as_view(), name='payment-settings'),
]
