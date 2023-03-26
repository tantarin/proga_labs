from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=200, default='Ivan')

    last_name = models.CharField(max_length=200, default='Ivanov')

    age = models.IntegerField(default=20)

    date_of_birth = models.DateField(name='dob')

    password = models.CharField(max_length=8, default='123')

    email = models.EmailField(max_length=75, default='from@example.com', )

    def __str__(self):
        return self.first_name + ', ' + self.date_of_birth
