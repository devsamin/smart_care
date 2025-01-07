from django.shortcuts import render
from rest_framework import viewsets
from .models import Service
from . import serializers 
# Create your views here.

# object gula k jasone convert korbe
class ServiceViewset(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = serializers.ServiceSerializer