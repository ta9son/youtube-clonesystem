from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny

from .serializers import UserSerializer, VideoSerializer
from .models import Video


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


