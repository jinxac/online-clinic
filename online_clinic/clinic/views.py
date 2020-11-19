from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_201_CREATED
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser
from rest_framework.exceptions import ValidationError


from .models import Clinic,Role, Employee, EmployeeRole, InDepartment, Department, Schedule
from .serializer import ClinicSerializer

"""
1. Get schedule for all doctors in a department
2. Add entry to schedule
3. Delete schedule
4. Update schedule
5. Get schedule for a doctor in department


1. Allow patients to make appointments/ patient cases
2. Multiple appointments for a a patience case
3. Cancel appointment
4. Check appointment history for a patient
5. Upload documents from patient
6. Map document to an appointment
7. Share document with other clinic
8. Revoke access to old documents
"""



@api_view(['POST'])
def assign_user_to_department(request):
  user = request.data['user']

  if not user:
    raise ValidationError("Please pass user")

  department = Department.objects.get(
    name=request.data['department'],
    clinic=request.data['clinic']
  )

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

  InDepartment.object.create(
    employee=employee,
    department=department
  )

  return Response({"message": "User assigned to clinic", "status": HTTP_201_CREATED})

# Create your views here.
@api_view(['POST'])
def register_user(request):
  user = User.objects.create(
    email=request.data['email'],
    username=request.data['username']
  )
  user.set_password(request.data['password'])

  return Response({"message": "User created!", "status": HTTP_201_CREATED})

class ClinicList(generics.ListCreateAPIView):
  serializer_class = ClinicSerializer
  permission_classes = [IsAdminUser]
  queryset = Clinic.objects.all()