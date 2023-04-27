from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Category


@receiver(post_save, sender=User)
def create_default_categories(sender, instance, created, **kwargs):
    if created:
        default_categories = [
            'Food and Dining',
            'Transportation',
            'Housing',
            'Utilities',
            'Entertainment',
            'Personal Care',
            'Shopping',
            'Health and Fitness',
            'Travel'
            ]
        for category_name in default_categories:
            Category.objects.create(user=instance, name=category_name)
