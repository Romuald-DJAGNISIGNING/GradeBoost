from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout

from .models import User
from .serializers import UserSerializer, RegisterSerializer, TutorProfileSerializer

from reviews.models import Review
from django.db.models import Avg


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


from django.shortcuts import render

@login_required
def show_home_location(request):
    if request.user.home_location:
        lat, lng = request.user.home_location.split(',')
        location = (lat, lng)
    else:
        location = None
    return render(request, 'users/show_location.html', {'location': location})

@login_required
def set_home_location(request):
    if request.method == 'POST':
        lat = request.POST.get('latitude')
        lng = request.POST.get('longitude')
        if lat and lng:
            request.user.home_location = f"{lat},{lng}"
            request.user.save()
            return redirect('dashboard')  # Redirect to your dashboard after saving
    return render(request, 'users/location_picker.html')


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class UserDetailView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class LoginView(APIView):
    def post(self, request):
        identifier = request.data.get('identifier')
        password = request.data.get('password')
        user = None

        # Try all possible login methods
        try:
            user = User.objects.get(email=identifier)
        except User.DoesNotExist:
            try:
                user = User.objects.get(username=identifier)
            except User.DoesNotExist:
                try:
                    user = User.objects.get(phone=identifier)
                except User.DoesNotExist:
                    return Response({'error': 'Invalid credentials'}, status=401)

        if user and user.check_password(password):
            if not user.is_active:
                return Response({'error': 'Account is inactive'}, status=403)
            login(request, user)
            return Response({'message': 'Login successful'})
        return Response({'error': 'Invalid credentials'}, status=401)

class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({'message': 'Logged out'})

class TopTutorsListView(generics.ListAPIView):
    serializer_class = TutorProfileSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return User.objects.filter(role='tutor').annotate(avg_rating=Avg('received_reviews__rating')).order_by('-avg_rating')
