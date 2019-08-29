from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.core.validators import validate_email
from django.contrib.auth.hashers import check_password, make_password

from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view, renderer_classes, permission_classes

from .rest_utils import IsAuthenticated, AllowAny, viewsets, generics, APIView, parsers
from .models import PS2User, Token
from ps2auth.backends import PS2AuthBackend

import json

# Create your VIEWS here.

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    print(request.META.get('HTTP_AUTHORIZATION'))
    if request.META.get('HTTP_AUTHORIZATION'):
        token = request.META.get('HTTP_AUTHORIZATION').split(' ')[1]
        print(Token.objects.get(key=token))
        user = PS2AuthBackend.authenticate(request, email=None, password=None, token=token)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key},
            status=200
        )
    json.loads(request.body.decode('utf-8'))
    email, password = request.data['mail'], request.data['password']
    if email is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=400)
    user = PS2User.objects.get(email=email)
    print(get_user_model())
    print(user)
    print(user.password)
    print(check_password(password, user.password))
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=404)
    if check_password(password, user.password):
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key},
                        status=200)


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def register(request):
    json.loads(request.body.decode('utf-8'))
    email, password = request.data['mail'], request.data['password']
    if email is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=400)
    user = PS2AuthBackend.authenticate(request, email=email, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=404)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=200)