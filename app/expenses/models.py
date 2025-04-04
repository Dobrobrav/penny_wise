from django.db import models


# Create your models here.
class Expense(models.Model):
    name = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
