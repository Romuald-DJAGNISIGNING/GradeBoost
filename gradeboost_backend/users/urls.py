
from django.urls import path
from .views import RegisterView, LoginView, LogoutView, UserDetailView
from .views import set_home_location
from .views import show_home_location



urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('me/', UserDetailView.as_view(), name='user-detail'),
    path('set-location/', set_home_location, name='set_location'),
    path('view-location/', show_home_location, name='view_location'),
]
