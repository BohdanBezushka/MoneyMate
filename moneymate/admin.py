from django.contrib import admin
from django.db.models import Sum
from .models import Expense, Category, Origin, Income, Currency


# Register your models here:
# Category and Expense:
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'amount', 'category', 'description')
    list_filter = ('user', 'category')
    ordering = ('user', 'category')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'name')
    list_filter = ('user', 'name')
    ordering = ('user', 'name')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Expense, ExpenseAdmin)


# Origin and Income:
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'amount', 'origin', 'description')
    list_filter = ('user', 'origin')
    ordering = ('user', 'origin')


class OriginAdmin(admin.ModelAdmin):
    list_display = ('user', 'name')
    list_filter = ('user', 'name')
    ordering = ('user', 'name')


admin.site.register(Origin, OriginAdmin)
admin.site.register(Income, IncomeAdmin)


# Currency:
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('user', 'currency', 'abbreviation', 'symbol')
    list_filter = ('user', 'currency', 'abbreviation', 'symbol')
    ordering = ('user', 'currency', 'abbreviation', 'symbol')


admin.site.register(Currency, CurrencyAdmin)
