from online_clinic.clinic.models import Employee, EmployeeRole, Role
from django.contrib.auth.models import User


mock_data = [
  {
    "role": "D",
    "email": "doctor1@amail.com",
    "username": "doctor1",
    "first_name": "Doctor 1 first",
    "last_name": "Doctor 1 last",
    "gender": "M",
    "phone_number": "123456789",
    "permanent_address": "test address",
    "password": "admin123"
  },
  {
    "role": "D",
    "email": "doctor2@amail.com",
    "username": "doctor2",
    "first_name": "Doctor 2 first",
    "last_name": "Doctor 2 last",
    "gender": "M",
    "phone_number": "123456789",
    "permanent_address": "test address",
    "password": "admin123"
  },
  {
    "role": "D",
    "email": "doctor3@amail.com",
    "username": "doctor3",
    "first_name": "Doctor 3 first",
    "last_name": "Doctor 3 last",
    "gender": "M",
    "phone_number": "123456789",
    "permanent_address": "test address",
    "password": "admin123"
  },
  {
    "role": "A",
    "email": "assistant1@amail.com",
    "username": "assistant1",

    "first_name": "Assistant 1 first",
    "last_name": "Assistant 1 last",
    "gender": "M",
    "phone_number": "123456789",
    "permanent_address": "test address",
    "password": "admin123"
  },
  {
    "role": "A",
    "email": "assistant2@amail.com",
    "username": "assistant2",
    "first_name": "Assistant 2 first",
    "last_name": "Assistant 2 last",
    "gender": "M",
    "phone_number": "123456789",
    "permanent_address": "test address",
    "password": "admin123"
  },
  {
    "role": "A",
    "username": "assistant3",
    "email": "assistant3@amail.com",
    "first_name": "Assistant 3 first",
    "last_name": "Assistant 3 last",
    "gender": "M",
    "phone_number": "123456789",
    "permanent_address": "test address",
    "password": "admin123"
  }
]

def create_user():
  for datum in mock_data:
    user = User.objects.create(
      email=datum['email'],
      username=datum['username']
    )
    user.set_password(datum['password'])

    role = Role.objects.get(role_name=datum['role'])

    employee = Employee.objects.create(
      user=user,
      first_name=datum['first_name'],
      last_name=datum['last_name'],
      gender=datum['gender'],
      phone_number=datum['phone_number'],
      permanent_address=datum['permanent_address']
    )

    EmployeeRole.objects.create(
      employee=employee,
      role=role
    )