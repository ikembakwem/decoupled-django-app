from django.db.models import CharField
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  name = CharField(blank=True ,max_length=100)

  def __str__(self):
    return self.email
