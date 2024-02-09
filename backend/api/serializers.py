from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import User, Video


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ['email', 'password', 'username', 'id']
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}
    
    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)

class VideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Video
        fields = ['id', 'title', 'video', 'thum', 'like', 'dislike']

