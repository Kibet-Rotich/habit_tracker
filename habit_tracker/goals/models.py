from django.db import models
from users.models import User

class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=50, choices=[('weekly', 'Weekly'), ('monthly', 'Monthly'), ('yearly', 'Yearly')])
    deadline = models.DateField()
    status = models.CharField(max_length=50, choices=[('ongoing', 'Ongoing'), ('completed', 'Completed')])
    is_public = models.BooleanField(default=False)

class Task(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=50, choices=[('completed', 'Completed'), ('not_completed', 'Not Completed')])
