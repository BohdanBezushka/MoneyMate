from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from django.utils.timezone import now


# Create your models here:
# This is the database for expenses/categories.
class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=now)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=40)
    description = models.TextField(max_length=140)

    def __str__(self):
        return self.category


class Category(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


# This is the database for incomes/ origins.
class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=now)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    origin = models.CharField(max_length=40)
    description = models.TextField(max_length=140)

    def __str__(self):
        return self.origin


class Origin(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Origins'

    def __str__(self):
        return self.name


# This is the database for currencies.
class Currency(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    currency = models.CharField(max_length=30)
    abbreviation = models.CharField(max_length=10)
    symbol = models.CharField(max_length=5)
    is_choosen = models.BooleanField(default=False)

    def __str__(self):
        return self.currency
