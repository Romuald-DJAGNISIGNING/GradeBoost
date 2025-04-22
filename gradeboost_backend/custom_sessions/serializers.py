

from rest_framework import serializers
from .models import Session

class custom_sessionserializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = '__all__'
        read_only_fields = ['is_approved', 'is_canceled']
