from django.db import models
from users.models import User

class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    description = models.TextField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_public = models.BooleanField(default=False)

class HabitTracking(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    habit_name = models.CharField(max_length=255)
    start_date = models.DateField()
    completion_log = models.JSONField()  # Stores date and status
    streaks = models.IntegerField(default=0)
