from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt

from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view, renderer_classes, permission_classes

from .rest_utils import UserSerializer, IsAuthenticated, AllowAny, viewsets, generics, APIView, parsers
from .models import PS2User, Token
from ps2auth.backends import PS2AuthBackend

import json
from urllib.parse import unquote

# Create your views here.

User = get_user_model()


@csrf_exempt                        # CSRFs are more or less irrelevant for mobile clients
@api_view(['POST'])                 # A login endpoint needs credentials, so only POST is allowed
@renderer_classes([JSONRenderer])   # Without the renderer class Response does not know how to render the data
@permission_classes([AllowAny])     # A user that wants to log in can't be authenticated
def login(request):
    # request.body is a byte stream, that's why we have to decode it to utf-8
    data = json.loads(request.body.decode('utf-8'))
    ps2auth = PS2AuthBackend()
    # ps2auth returns the user obj if authentication is successful
    user = ps2auth.authenticate(data['mail'], data['password'])
    if user is not None:
        # Create token for user
        token, created = Token.objects.get_or_create(user=user)
        if created is False:
            # If the user already has a token delete it and establish a new one
            Token.objects.filter(user=user).delete()
            token, create = Token.objects.get_or_create(user=user)
        # Render the response, it takes the renderer_class from the decorator and creates a json.
        # The client should take the user_id for reference and save the token for authentication.
        # This token will be added to every request from the client.
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
    else:
        return Response({
            'token': 'Invalid credentials.'
        })

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = PS2User.objects.all()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        if request.user.is_staff:
            queryset = PS2User.objects.all()
            serializer = UserSerializer(queryset, many=True, context={'request': request})
            return Response(serializer.data)
        else:
            # If not admin only return the authenticated user.
            return self.retrieve(request, get_self=True)

    def retrieve(self, request, *args, **kwargs):
        if kwargs['get_self'] is True:
            queryset = PS2User.objects.get(pk=request.user.pk)
            serializer = UserSerializer(queryset, many=False, context={'request': request})
            return Response(serializer.data)
        pass

    def update(self, request, *args, **kwargs):
        pass

    def partial_update(self, request, *args, **kwargs):
        pass

    def destroy(self, request, *args, **kwargs):
        pass


@csrf_exempt
class UserCreateView(APIView):
    model = get_user_model()
    permission_classes = [
        AllowAny  # Or anon users can't register
    ]
    serializer_class = UserSerializer