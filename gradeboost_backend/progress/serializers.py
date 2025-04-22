

from rest_framework import serializers
from .models import StudentProgress

class StudentProgressSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source='student.username', read_only=True)
    tutor_name = serializers.CharField(source='tutor.username', read_only=True)

    class Meta:
        model = StudentProgress
        fields = '__all__'
        read_only_fields = ['tutor']
