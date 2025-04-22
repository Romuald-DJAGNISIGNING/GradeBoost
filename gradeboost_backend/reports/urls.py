

from django.urls import path
from .views import CreateReportView, ListReportsView, UpdateReportStatusView

urlpatterns = [
    path('create/', CreateReportView.as_view(), name='create-report'),
    path('admin/list/', ListReportsView.as_view(), name='list-reports'),
    path('admin/update/<int:pk>/', UpdateReportStatusView.as_view(), name='update-report-status'),
]
