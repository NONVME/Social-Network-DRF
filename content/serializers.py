from rest_framework.serializers import ModelSerializer, SlugRelatedField

from .models import Post, PostRate


class PostSerializer(ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)
    # evaluator = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Post
        fields = '__all__'


class PostRateSerializer(ModelSerializer):
    class Meta:
        model = PostRate
        fields = ('like', 'post')
