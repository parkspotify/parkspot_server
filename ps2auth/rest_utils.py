from django.conf.urls import url, include
from .models import PS2User
from .backends import PS2AuthBackend

from rest_framework import routers, serializers, viewsets, permissions, generics, parsers
from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, AllowAny


# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):

    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = PS2User
        fields = ['id', 'email', 'password']

    def create(self, validated_data):
        print(validated_data)
        user = PS2User.objects.create(
            email=validated_data['mail']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


