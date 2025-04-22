

from django.urls import path
from .views import AdminDashboardView, TutorDashboardView, StudentDashboardView

urlpatterns = [
    path('admin/', AdminDashboardView.as_view(), name='admin-dashboard'),
    path('tutor/', TutorDashboardView.as_view(), name='tutor-dashboard'),
    path('student/', StudentDashboardView.as_view(), name='student-dashboard'),
]
