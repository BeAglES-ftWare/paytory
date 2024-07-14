from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Token(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=48)

    def __str__(self):
        return f"{self.user}-token"

class Expense(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, models.CASCADE)

    def __str__(self):
        return f"{self.date}-{self.amount}"


class Income(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, models.CASCADE)

    def __str__(self):
        return f"{self.date}-{self.amount}"
