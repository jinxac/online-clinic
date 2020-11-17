from online_clinic.clinic.models import Clinic

mock_data = [
    {
        "name": "Test Clinic 1",
        "address": "First Street Address"
    },
    {
        "name": "Test Clinic 2",
        "address": "Second Street Address",
    },
    {
        "name": "Test Clinic 3",
        "address": "Third Street Address"
    }
]


def create_clinic():
    for datum in mock_data:
        Clinic.objects.create(
            name=datum['name'],
            address=datum['address']
        )
