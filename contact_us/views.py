from django.shortcuts import render
from rest_framework import viewsets
from .models import ContactUs
from . import serializers 
# Create your views here.

# object gula k jasone convert korbe
class ContactViewset(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = serializers.ContactUsSerializer