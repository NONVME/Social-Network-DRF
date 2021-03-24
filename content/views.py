from rest_framework.mixins import UpdateModelMixin
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from .models import Post, PostRate
from .serializers import PostSerializer, PostRateSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostRateView(UpdateModelMixin, GenericViewSet):
    queryset = PostRate.objects.all()
    serializer_class = PostRateSerializer
