from django.conf import settings
from django.db import models
from django.utils import timezone


class User(models.Model):
    first_name = models.CharField(max_length=200)
    date_of_birth = models.DateField(name='dob')

    def __str__(self):
        return self.first_name + ', ' + self.date_of_birth