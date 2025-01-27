from django.db import models
from users.models import User
from goals.models import Goal

class AccountabilityGroup(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

class GroupMembership(models.Model):
    group = models.ForeignKey(AccountabilityGroup, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class SharedGoal(models.Model):
    group = models.ForeignKey(AccountabilityGroup, on_delete=models.CASCADE)
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
