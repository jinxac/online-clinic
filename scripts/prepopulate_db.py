import django
django.setup()

from .create_role import create_role
from .create_department import create_department
from .create_user import create_user
from .create_clinic import create_clinic


def init():
  create_clinic()
  create_role()
  create_department()
  create_user()
init()