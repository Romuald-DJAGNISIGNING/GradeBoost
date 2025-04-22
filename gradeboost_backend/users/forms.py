from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Profile
from allauth.account.forms import SignupForm
from django.core.exceptions import ValidationError

# Custom user registration form
class UserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=15, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'phone_number']

# Custom login form
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

# Profile form for updating profile information
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture', 'bio', 'location', 'transcript', 'timetable', 'is_tutor', 'subjects']
        widgets = {
            'profile_picture': forms.ClearableFileInput(attrs={'multiple': True}),
        }

# Form for tutor's subjects and timetable
class TutorForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['transcript', 'subjects', 'is_tutor']

class CustomSignupForm(SignupForm):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('tutor', 'Tutor'),
    ]
    role = forms.ChoiceField(choices=ROLE_CHOICES, required=True)
    phone = forms.CharField(max_length=15, required=True)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and not email.endswith('@gmail.com'):
            raise ValidationError("Only Gmail addresses are allowed.")
        return email

    def save(self, request):
        user = super().save(request)
        user.role = self.cleaned_data['role']
        user.phone = self.cleaned_data['phone']
        user.save()
        return user
