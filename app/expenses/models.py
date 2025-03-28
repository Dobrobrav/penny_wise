from django.db import models


# Create your models here.
class Expense(models.Model):
    name = models.CharField(max_length=100)
    cost = models.CharField(max_length=20)
    category = models.CharField(max_length=100)
