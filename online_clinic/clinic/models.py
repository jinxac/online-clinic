from django.db import models
from djchoices.choices import DjangoChoices, ChoiceItem
from django.core.validators import MinLengthValidator

# Create your models here.

class GenderType(DjangoChoices):
  Male = ChoiceItem("M")
  Female = ChoiceItem("F")
  Other = ChoiceItem("O")

class RoleType(DjangoChoices):
  Doctor = ChoiceItem("D")
  Assistant = ChoiceItem("A")
  Nurse = ChoiceItem("N")

class Clinic(models.Model):
  name =  models.CharField(max_length=100)
  address = models.CharField(max_length=255)
  details = models.CharField(max_length=255, blank=True)


class Department(models.Model):
  name = models.CharField(max_length=100)
  clinic_id = models.ForeignKey(Clinic, on_delete=models.CASCADE)

class Employee(models.Model):
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  gender = models.CharField(max_length=1, choices=GenderType.choices, validators=[GenderType.validator])
  email = models.EmailField(max_length=254)
  phone_number = models.CharField(max_length=15, validators=[MinLengthValidator(8)])
  permanent_address = models.CharField(max_length=255)
  is_active = models.BooleanField(default=True)

class InDepartment(models.Model):
  start_at = models.DateTimeField(auto_now_add=True)
  end_at = models.DateTimeField(null=True, blank=True)
  is_active = models.BooleanField(default=True)
  employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
  department = models.ForeignKey(Department, on_delete=models.CASCADE)

class Role(models.Model):
  role_name = models.CharField(max_length=10, choices=RoleType.choices, validators=[RoleType.validator])

class EmployeeRole(models.Model):
  employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
  role_id = models.ForeignKey(Role, on_delete=models.CASCADE)
  start_at = models.DateTimeField(auto_now_add=True)
  end_at = models.DateTimeField(null=True, blank=True)
  is_active = models.BooleanField(default=True)


class Schedule(models.Model):
  in_department = models.ForeignKey(InDepartment, on_delete=models.CASCADE)
  date = models.DateField(auto_now_add=True)
  start_time = models.TimeField(auto_now_add=True)
  end_time = models.TimeField(null=True, blank=True)
