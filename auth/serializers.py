from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True
    )

    class Meta:
        model = User
        fields = '__all__'
