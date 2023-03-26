from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=200)

    last_name = models.CharField(max_length=200)

    date_of_birth = models.DateField(name='dob')

    password = models.TextField()

    email = models.EmailField(max_length=75)

    def __str__(self):
        return self.first_name + ', ' + self.date_of_birth
