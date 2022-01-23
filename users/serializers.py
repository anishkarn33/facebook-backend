from .models import User, UserProfile
from rest_framework import serializers



class UserSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(min_length=10)
    password = serializers.CharField(allow_blank=True, write_only=True)
    class Meta:
        model = User
        fields = ['id','username','email', 'first_name', 'last_name', 'password','is_staff', 'is_superuser', 'is_active', 'date_joined', 'last_login','phone']
        read_only_fields = ['id', 'is_staff', 'is_superuser', 'is_active', 'date_joined', 'last_login']
        extra_kwargs = {'password': {'write_only': True}}


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'first_name', 'middle_name', 'last_name', 'dob', 'email',  'phone', 'user','avatar','bio','address']