from django.db import models
from decimal import Decimal
from djchoices.choices import DjangoChoices, ChoiceItem

from online_clinic.clinic.models import Department

class StatusType(DjangoChoices):
  Created = ChoiceItem("CR")
  InProgress = ChoiceItem("IP")
  Postpone = ChoiceItem("PO")
  Cancelled = ChoiceItem("CA")



# Create your models here.
class Patient(models.Model):
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  address = models.CharField(max_length=255)

class PatientCase(models.Model):
  patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
  start_at = models.DateTimeField(auto_now_add=True)
  end_at = models.DateTimeField(blank=True, null=True)
  in_progress = models.BooleanField(default=True)
  total_cost = models.DecimalField(max_digits=10, decimal_places=6, default=Decimal('0.000000'))
  amount_paid = models.DecimalField(max_digits=10, decimal_places=6, default=Decimal('0.000000'))


class AppointmentStatus(models.Model):
  status_name = models.CharField(max_length=2, choices=StatusType.choices, validators=[StatusType.validator])

class Appointment(models.Model):
  patient_case = models.ForeignKey(PatientCase, on_delete=models.CASCADE)
  in_department = models.ForeignKey(Department, on_delete=models.CASCADE)
  appointment_status = models.ForeignKey(AppointmentStatus, on_delete=models.CASCADE)

