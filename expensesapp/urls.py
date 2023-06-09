"""expensesapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from moneymate import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homePage, name='base'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('accounts/', include('allauth.urls')),

    # Create, read, update and delete EXPENSES:
    path('expenses/', views.viewExpensesList, name='listExpenses'),
    path('addexpense/', views.addExpense, name='addExpense'),
    path('editexpense/<int:id>', views.editExpense, name='edit-expense'),
    path('deleteExpense/<int:id>', views.deleteExpense, name='delete-expense'),

    # Create, read, update and delete INCOMES:
    path('incomes/', views.viewIncomesList, name='listIncomes'),
    path('addincome/', views.addIncome, name='addIncome'),
    path('editincome/<int:id>', views.editIncome, name='edit-income'),
    path('deleteincome/<int:id>', views.deleteIncome, name='delete-income'),

    # Create, read, update and delete CATEGORIES:
    path('categories/', views.viewCategoriesList, name='listCategories'),
    path('addcategory/', views.addCategory, name='addCategory'),
    path('editcategory/<int:id>', views.editCategory, name='edit-category'),
    path(
        'deletecategory/<int:id>',
        views.deleteCategory,
        name='delete-category'),

    # Create, read, update and delete Origins:
    path('origins/', views.viewOriginsList, name='listOrigins'),
    path('addorigin/', views.addOrigin, name='addOrigin'),
    path('editorigin/<int:id>', views.editOrigin, name='edit-origin'),
    path('deleteorigin/<int:id>', views.deleteOrigin, name='delete-origin'),

    # Create, read, update and delete Currencies:
    path('currencies/', views.viewCurrenciesList, name='listCurrencies'),
    path('addcurrency/', views.addCurrency, name='addCurrency'),
    path('editcurrency/<int:id>', views.editCurrency, name='edit-currency'),
    path(
        'deletecurrency/<int:id>',
        views.deleteCurrency,
        name='delete-currency'),
    path('choosecurrency', views.chooseCurrency, name='choose-currency'),
]
