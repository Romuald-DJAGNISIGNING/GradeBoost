import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'your-secret-key'

DEBUG = True

ALLOWED_HOSTS = []

# Installed apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

     # Your other apps
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    
    #'storages', For cloud storage later

    # Project apps

    'users',
    'custom_sessions',
    'dashboard',
    'messaging',
    'payments',
    'reviews',
    'reports',
    'progress',
    # Third-party
    'rest_framework',
    'corsheaders',
    'social_django',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # Corrected line
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'gradeboost.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends', 
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'gradeboost.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Change to PostgreSQL/MySQL if needed
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Douala'

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",  # Ensure this directory exists
]
STATIC_ROOT = BASE_DIR / "staticfiles"
TEMPLATESFILES_DIRS = [BASE_DIR / 'templates',]

# Media config
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Custom user model
AUTH_USER_MODEL = 'users.User'

# Allauth settings
SITE_ID = 1  # Required for Django Allauth
ACCOUNT_LOGIN_METHODS = ['username', 'email', 'phone']  # Allow login with username, email, or phone
ACCOUNT_SIGNUP_FIELDS = ['username', 'email*', 'phone', 'password1', 'password2']  # Fields required during signup   
ACCOUNT_EMAIL_VERIFICATION = 'mandatory' # Require email verification  
ACCOUNT_FORMS = {
    'signup': 'users.forms.CustomSignupForm',  # Custom signup form
}

CSRF_USE_SESSIONS = False

# Social Auth Settings
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '<774631068431-u2i657s26pr1anlrqi1d3l5h7dbi4kee.apps.googleusercontent.com>'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '<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>'
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': ['profile', 'email'],
        'AUTH_PARAMS': {'access_type': 'online'},
        'OAUTH_PKCE_ENABLED': True,
    }
}

# Login/Logout URLs
LOGIN_REDIRECT_URL = '/'  # Where users are redirected after login
LOGOUT_REDIRECT_URL = '/'  # Where users are redirected after logout

# API placeholders (to be integrated in `payments` app later)
ORANGE_MONEY_API_KEY = 'your-orange-api-key'
MTN_MOBILE_MONEY_API_KEY = 'your-mtn-api-key'



AUTHENTICATION_BACKENDS = [
    'users.backends.PhoneUsernameOrEmailBackend',  # Custom backend
    'allauth.account.auth_backends.AuthenticationBackend',  # Allauth backend
    'django.contrib.auth.backends.ModelBackend',  # Default backend
]

