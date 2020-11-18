from online_clinic.clinic.models import Role


mock_data = [
  {
    "role_name": "D"
  },
  {
    "role_name": "N"
  },
  {
    "role_name": "A"
  }
]


def create_role():
  for datum in mock_data:
    Role.objects.create(
        role_name=datum['role_name']
    )

