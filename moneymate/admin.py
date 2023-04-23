from django.contrib import admin
from django.db.models import Sum
from .models import Expense, Category, Origin, Income

# Register your models here:
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'amount', 'category', 'description')
    list_filter = ('user', 'category')
    ordering = ('user','category')

admin.site.register(Category)
admin.site.register(Expense, ExpenseAdmin)

class IncomeAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'amount', 'origin', 'description')
    list_filter = ('user', 'origin')
    ordering = ('user','origin')

admin.site.register(Origin)
admin.site.register(Income, IncomeAdmin)