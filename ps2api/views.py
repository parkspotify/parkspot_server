from django.shortcuts import render

from django.contrib.auth.models import User

from ps2api.models import Raspberry
from ps2api.serializers.RaspberrySerializer import RaspberrySerializer

from rest_framework import generics, viewsets, mixins
from rest_framework.permissions import IsAdminUser

# Create your views here.


class RaspberryViewSet(viewsets.GenericViewSet,  # generic view functionality
                     mixins.CreateModelMixin,  # handles POSTs
                     mixins.RetrieveModelMixin,  # handles GETs for 1 Company
                     mixins.UpdateModelMixin,  # handles PUTs and PATCHes
                     mixins.ListModelMixin):  # handles GETs for many Companies

    serializer_class = RaspberrySerializer
    queryset = Raspberry.objects.all()

"""
class RaspberryList(generics.ListCreateAPIView):
    queryset = Raspberry.objects.all()
    serializer_class = RaspberrySerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class RaspberryDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RaspberrySerializer

    def get_queryset(self):
        return Raspberry.objects.all().filter(user=self.request.user)
"""
