from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db import models

from sem_7.lab_microservices.mysite.polls.models import Question, Choice


class Chart(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateField()
    responsible = models.ForeignKey(User, on_delete=models.CASCADE)
    week_number = models.CharField(max_length=2, blank=True)
    finish_date = models.DateField()

#string representation method
    def __str__(self):
        return str(self.name)
#overiding the save method
    def save(self, *args, **kwargs):
        print(self.start_date.isocalendar()[1])
        if self.week_number == "":
            self.week_number = self.start_date.isocalendar()[1]
        super().save(*args, **kwargs)


class VotingStatistics(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    votes_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.question.question_text} - {self.choice.choice_text}: {self.votes_count} votes"