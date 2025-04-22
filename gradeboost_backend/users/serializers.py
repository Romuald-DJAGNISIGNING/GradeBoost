

from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ['id', 'role', 'is_suspended', 'warning_count']

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'phone', 'password', 'first_name', 'last_name', 'gender', 'role', 'id_card', 'profile_pic')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            phone=validated_data['phone'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            gender=validated_data.get('gender'),
            role=validated_data['role'],
            id_card=validated_data['id_card'],
            profile_pic=validated_data.get('profile_pic'),
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class TutorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'profile_pic', 'transcript', 'subjects']  # Add fields relevant to tutors