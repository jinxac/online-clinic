from online_clinic.clinic.models import Department, Clinic

mock_data = [
  {
    "name": "Pediatrics"
  },
  {
    "name": "Dermatology"
  },
  {
    "name": "General Physician"
  }
]


def create_department():
  try:
    clinic = Clinic.objects.get(id=1)
  except:
    return None

  for datum in mock_data:
    Department.objects.create(
      name=datum['name'],
      clinic=clinic
    )
