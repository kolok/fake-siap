from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    cerbere_uid = models.IntegerField(null=True)

    def __str__(self):
        return (
            f"{self.first_name} {self.last_name}".strip()
            if self.first_name or self.last_name
            else self.username
        )

