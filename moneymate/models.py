from django.db import models
from django.contrib.auth.models import User

from django.utils.timezone import now

# Create your models here:

# This is the database for user expenses.
class addExpense(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    date = models.DateField(default=now)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50)
    description = models.TextField(max_length=300)

    def __str__(self):
        return self.category

class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

