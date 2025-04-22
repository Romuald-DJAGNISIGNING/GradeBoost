

from django.urls import path
from .views import AddProgressView, StudentProgressListView

urlpatterns = [
    path('add/', AddProgressView.as_view(), name='add-progress'),
    path('my-progress/', StudentProgressListView.as_view(), name='student-progress'),
]
