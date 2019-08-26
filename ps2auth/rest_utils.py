from django.conf.urls import url, include
from .models import PS2User
from .backends import PS2AuthBackend

from rest_framework import routers, serializers, viewsets, permissions, generics, parsers
from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, AllowAny
from django.views.decorators.csrf import csrf_exempt


