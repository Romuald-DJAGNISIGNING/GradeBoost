# gradeboost/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/custom_sessions/', include('custom_sessions.urls')),
    path('api/dashboard/', include('dashboard.urls')),
    path('api/messaging/', include('messaging.urls')),
    path('api/payments/', include('payments.urls')),
    path('api/reviews/', include('reviews.urls')),
    path('api/reports/', include('reports.urls')),
    path('auth/', include('social_django.urls', namespace='social')),
    path('accounts/', include('allauth.urls')),  # Allauth URLs for login, logout, registration, etc.
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
