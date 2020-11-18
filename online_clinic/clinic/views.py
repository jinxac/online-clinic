from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_201_CREATED
from django.contrib.auth.models import User



from .models import Clinic,Role, Employee, EmployeeRole
from .serializer import ClinicSerializer

from rest_framework.permissions import IsAdminUser

# Create your views here.
@api_view(['POST'])
def register_user(request):
  user = User.objects.create(
    email=request.data['email'],
    username=request.data['username']
  )
  user.set_password(request.data['password'])

  role = Role.objects.get(role_name=request.data['role'])

  employee = Employee.objects.create(
    user=user,
    first_name=request.data['first_name'],
    last_name=request.data['last_name'],
    gender=request.data['gender'],
    phone_number=request.data['phone_number'],
    permanent_address=request.data['permanent_address']
  )

  EmployeeRole.objects.create(
    employee=employee,
    role=role
  )

  return Response({"message": "Hello, world!", "status": HTTP_201_CREATED})

class ClinicList(generics.ListCreateAPIView):
  serializer_class = ClinicSerializer
  permission_classes = [IsAdminUser]
  queryset = Clinic.objects.all()