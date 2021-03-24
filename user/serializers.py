from rest_framework.serializers import ModelSerializer

from .models import SiteUser


class UserSerializer(ModelSerializer):
    class Meta:
        model = SiteUser
        fields = '__all__'
