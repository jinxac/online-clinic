from django.shortcuts import render
from rest_framework import generics


from .models import Clinic
from .serializer import ClinicSerializer

from rest_framework.permissions import IsAdminUser

# Create your views here.


class ClinicList(generics.ListCreateAPIView):
  serializer_class = ClinicSerializer
  permission_classes = [IsAdminUser]
  queryset = Clinic.objects.all()