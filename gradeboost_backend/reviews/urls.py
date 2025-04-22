

from django.urls import path
from .views import ReviewCreateView, TutorReviewListView

urlpatterns = [
    path('create/', ReviewCreateView.as_view(), name='create-review'),
    path('tutor/<int:tutor_id>/', TutorReviewListView.as_view(), name='tutor-reviews'),
]
