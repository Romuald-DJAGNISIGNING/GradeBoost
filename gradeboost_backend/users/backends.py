from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

User = get_user_model()

class PhoneUsernameOrEmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Check if the username is a phone number
            user = User.objects.get(phone=username)
        except User.DoesNotExist:
            try:
                # Check if the username is an email
                user = User.objects.get(email=username)
            except User.DoesNotExist:
                try:
                    # Fallback to username
                    user = User.objects.get(username=username)
                except User.DoesNotExist:
                    return None

        if user.check_password(password):
            return user
        return None