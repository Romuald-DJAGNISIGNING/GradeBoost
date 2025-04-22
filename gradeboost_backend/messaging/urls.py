

from django.urls import path
from .views import SendMessageView, MessageListView

urlpatterns = [
    path('send/', SendMessageView.as_view(), name='send-message'),
    path('history/<int:contact_id>/', MessageListView.as_view(), name='message-history'),
]
