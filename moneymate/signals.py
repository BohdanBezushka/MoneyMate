from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Category, Origin


# New users have predefined categories for expenses
# and predefined origins for income.
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

        default_origins = [
            'Salary',
            'Investments',
            'Rental Income',
            'Freelance Income',
            'Side Hustle',
            'Grants and Scholarships',
            'Gifts and Inheritances',
            'Reimbursements',
            'Other Income']
        for origin_name in default_origins:
            Origin.objects.create(user=instance, name=origin_name)
