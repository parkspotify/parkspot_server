from django.contrib import admin
from django.urls import path, include

from rest_framework.authtoken import views as drf_auth_views

from . import views
from .rest_utils import routers
from .views import UserViewSet, UserCreateView

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'token/', drf_auth_views.obtain_auth_token),
    path(r'register/', UserViewSet.as_view({'post': 'create'}), name='register'),
    path(r'signin/', views.login, name='signin'),
    path(r'api/', include('rest_framework.urls', namespace='rest_framework')),
]