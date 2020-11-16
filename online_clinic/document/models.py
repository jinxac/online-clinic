from django.db import models
from djchoices.choices import DjangoChoices, ChoiceItem

from online_clinic.clinic.models import InDepartment
from online_clinic.patient.models import Appointment, Patient, PatientCase

class DocumentChoice(DjangoChoices):
  Pdf: ChoiceItem("PDF")

class DocumentType(models.Model):
  type_name = models.CharField(max_length=10, choices = DocumentChoice, validators=[DocumentChoice.validator])


class Document(models.Model):
  document_type = models.ForeignKey(DocumentType, on_delete=models.CASCADE)
  document_url = models.CharField(max_length=255)
  appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
  patient_case = models.ForeignKey(PatientCase, on_delete=models.CASCADE)
  in_department = models.ForeignKey(InDepartment, on_delete=models.CASCADE)


class DocumentShare(models.Model):
  document = models.ForeignKey(Document, on_delete=models.CASCADE)
  in_department = models.ForeignKey(InDepartment, on_delete=models.CASCADE)
