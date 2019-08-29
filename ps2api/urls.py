from django.urls import include, path

from rest_framework.routers import DefaultRouter
from .views import RaspberryViewSet

router = DefaultRouter()
router.register(r'raspberries', viewset=RaspberryViewSet, base_name='raspberry')

urlpatterns = [
    path(r'', include(router.urls)),
]