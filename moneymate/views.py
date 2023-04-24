from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .models import Category, Expense, Origin, Income
from django.contrib import messages
from django.db.models import Sum
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here:

def homePage(request):
    # This is the main page that will be displayed to the user.
    # The function has been exported to the 'expensesapp' 
    # project in the 'urls.py' file in order to visualize the HTML content.
    return render(request, 'moneymate/base.html')

def dashboard(request):
    # When the user logs in or registers, he/she will be taken 
    # directly to the templates/moneymate/dashboard.html file.
    expensesAmount = Expense.objects.filter(user=request.user)
    totalExpenses = sum(expense.amount for expense in expensesAmount)
    incomesAmount = Income.objects.filter(user=request.user)
    totalIncomes = sum(income.amount for income in incomesAmount)
    balance = totalIncomes - totalExpenses
    context = {'totalExpenses': totalExpenses, 'totalIncomes':totalIncomes, 'balance':balance}
    return render(request, 'moneymate/dashboard.html', context)

#                        EXPENSES            ----------

def viewExpensesList(request):
    # This feature allows the user to review the expenses
    # they have previously entered in the application. 
    # By clicking on 'Expenses' in the navigation bar of 
    # the dashboard.html, users can access a list of their recorded expenses.
    categories = Category.objects.all()
    expenses = Expense.objects.filter(user=request.user).order_by('-date')
    paginate = Paginator(expenses, 3)
    number_of_page = request.GET.get('page')
    page_object = paginate.get_page(number_of_page)
    expensesAmount = Expense.objects.filter(user=request.user)
    totalExpenses = sum(expense.amount for expense in expensesAmount)
    incomesAmount = Income.objects.filter(user=request.user)
    totalIncomes = sum(income.amount for income in incomesAmount)
    balance = totalIncomes - totalExpenses
    context = {'expenses': expenses, 'page_object': page_object, 'totalExpenses': totalExpenses, 'totalIncomes':totalIncomes, 'balance':balance}
    return render(request, 'moneymate/expenses/list_expenses.html', context)

def addExpense(request):
    # This feature enables users to access their expense records.
    # By clicking on the appropriate button
    expensesAmount = Expense.objects.filter(user=request.user)
    totalExpenses = sum(expense.amount for expense in expensesAmount)
    incomesAmount = Income.objects.filter(user=request.user)
    totalIncomes = sum(income.amount for income in incomesAmount)
    balance = totalIncomes - totalExpenses
    categories = Category.objects.all()
    context = {'categories': categories,'values': request.POST, 'totalExpenses': totalExpenses, 'totalIncomes':totalIncomes, 'balance':balance}
    if request.method == 'GET':
        return render(request, 'moneymate/expenses/add_expense.html', context)

    if request.method == 'POST':
        amount = request.POST['amount']

        if not amount:
            messages.error(request, 'Amount is required.')
            return render(request, 'moneymate/expenses/add_expense.html', context)
        description = request.POST['description']
        date = request.POST['date']
        category = request.POST['category']

        if not description:
            messages.error(request, 'Description is required.')
            return render(request, 'moneymate/expenses/add_expense.html', context)

        Expense.objects.create(user=request.user, amount=amount, date=date,category=category, description=description)
        messages.success(request, 'Expense saved successfully.')

        return redirect('listExpenses')

def editExpense(request, id):
    #The user will be able to edit the chosen expense.
    expensesAmount = Expense.objects.filter(user=request.user)
    totalExpenses = sum(expense.amount for expense in expensesAmount)
    incomesAmount = Income.objects.filter(user=request.user)
    totalIncomes = sum(income.amount for income in incomesAmount)
    balance = totalIncomes - totalExpenses
    expense = Expense.objects.get(pk=id)
    categories = Category.objects.all()
    context = {'expense': expense,'values': expense,'categories': categories, 'totalExpenses': totalExpenses, 'totalIncomes':totalIncomes, 'balance':balance }
    if request.method == 'GET':
        return render(request, 'moneymate/expenses/edit_expense.html', context)
    if request.method == 'POST':
        amount = request.POST['amount']

        if not amount:
            messages.error(request, 'Amount is required.')
            return render(request, 'moneymate/expenses/edit_expense.html', context)
        description = request.POST['description']
        date = request.POST['date']
        category = request.POST['category']

        if not description:
            messages.error(request, 'Description is required.')
            return render(request, 'moneymate/expenses/edit_expense.html', context)

        expense.user = request.user
        expense.amount = amount
        expense.date = date
        expense.category = category
        expense.description = description

        expense.save()
        messages.success(request, 'Expense updated  successfully.')

        return redirect('listExpenses')

def deleteExpense(request, id):
    # The user will be able to delete the chosen expense.
    expense = Expense.objects.get(pk=id)
    expense.delete()
    return redirect('listExpenses')


#                        INCOMES           ----------


def viewIncomesList(request):
    # This feature allows the user to review the incomes
    # they have previously entered in the application. 
    # By clicking on 'Incomes' in the navigation bar of 
    # the dashboard.html, users can access a list of their recorded incomes.
    expensesAmount = Expense.objects.filter(user=request.user)
    totalExpenses = sum(expense.amount for expense in expensesAmount)
    incomesAmount = Income.objects.filter(user=request.user)
    totalIncomes = sum(income.amount for income in incomesAmount)
    balance = totalIncomes - totalExpenses
    origins = Origin.objects.all()
    incomes = Income.objects.filter(user=request.user).order_by('-date')
    paginate = Paginator(incomes, 3)
    number_of_page = request.GET.get('page')
    page_object = paginate.get_page(number_of_page)
    context = {'incomes': incomes, 'page_object': page_object, 'totalExpenses': totalExpenses, 'totalIncomes':totalIncomes, 'balance':balance}
    return render(request, 'moneymate/incomes/list_incomes.html', context)

def addIncome(request):
    # This feature enables users to access their income records.
    # By clicking on the appropriate button.
    expensesAmount = Expense.objects.filter(user=request.user)
    totalExpenses = sum(expense.amount for expense in expensesAmount)
    incomesAmount = Income.objects.filter(user=request.user)
    totalIncomes = sum(income.amount for income in incomesAmount)
    balance = totalIncomes - totalExpenses
    origins = Origin.objects.all()
    context = {'origins': origins,'values': request.POST, 'totalExpenses': totalExpenses, 'totalIncomes':totalIncomes, 'balance':balance}
    if request.method == 'GET':
        return render(request, 'moneymate/incomes/add_income.html', context)

    if request.method == 'POST':
        amount = request.POST['amount']

        if not amount:
            return render(request, 'moneymate/incomes/add_income.html', context)
        description = request.POST['description']
        date = request.POST['date']
        origin = request.POST['origin']

        if not description:
            return render(request, 'moneymate/incomes/add_income.html', context)

        Income.objects.create(user=request.user, amount=amount, date=date, origin=origin, description=description)

        return redirect('listIncomes')

def editIncome(request, id):
    #The user will be able to edit the chosen income.
    expensesAmount = Expense.objects.filter(user=request.user)
    totalExpenses = sum(expense.amount for expense in expensesAmount)
    incomesAmount = Income.objects.filter(user=request.user)
    totalIncomes = sum(income.amount for income in incomesAmount)
    balance = totalIncomes - totalExpenses
    income = Income.objects.get(pk=id)
    origins = Origin.objects.all()
    context = {
        'income': income,
        'values': income,
        'origins': origins,
        'totalExpenses': totalExpenses, 
        'totalIncomes':totalIncomes, 
        'balance':balance
    }
    if request.method == 'GET':
        return render(request, 'moneymate/incomes/edit_income.html', context)
    if request.method == 'POST':
        amount = request.POST['amount']

        if not amount:
            return render(request, 'moneymate/incomes/edit_income.html', context)
        description = request.POST['description']
        date = request.POST['date']
        origin = request.POST['origin']

        if not description:
            return render(request, 'moneymate/incomes/edit_income.html', context)

        income.user = request.user
        income.amount = amount
        income.date = date
        income.origin = origin
        income.description = description

        income.save()

        return redirect('listIncomes')

def deleteIncome(request, id):
    # The user will be able to delete the chosen expense.
    income = Income.objects.get(pk=id)
    income.delete()
    return redirect('listIncomes')


#                        CATEGORIES          ----------
@login_required
def viewCategoriesList(request):
    # This feature allows the user to review the categories
    # they have previously entered in the application. 
    # By clicking on 'Categiry' in the navigation bar of 
    # the dashboard.html, users can access a list of their recorded categories.
    expensesAmount = Expense.objects.filter(user=request.user)
    totalExpenses = sum(expense.amount for expense in expensesAmount)
    incomesAmount = Income.objects.filter(user=request.user)
    totalIncomes = sum(income.amount for income in incomesAmount)
    balance = totalIncomes - totalExpenses
    categories = Category.objects.all()
    paginate = Paginator(categories, 3)
    number_of_page = request.GET.get('page')
    page_object = paginate.get_page(number_of_page)
    context = {'categories': categories, 'page_object': page_object, 'totalExpenses': totalExpenses, 'totalIncomes':totalIncomes, 'balance':balance}
    return render(request, 'moneymate/categories/list_categories.html', context)

@login_required
def addCategory(request):
    # This feature enables users to access their categories.
    # By clicking on the appropriate button.
    expensesAmount = Expense.objects.filter(user=request.user)
    totalExpenses = sum(expense.amount for expense in expensesAmount)
    incomesAmount = Income.objects.filter(user=request.user)
    totalIncomes = sum(income.amount for income in incomesAmount)
    balance = totalIncomes - totalExpenses
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'values': request.POST,
        'totalExpenses': totalExpenses, 
        'totalIncomes':totalIncomes, 
        'balance':balance,
    }
    if request.method == 'GET':
        return render(request, 'moneymate/categories/add_category.html', context)

    if request.method == 'POST':
        name = request.POST['name']

        if not name:
            return render(request, 'moneymate/categories/add_category.html', context)

        Category.objects.create(name=name)

        return redirect('listCategories')

@login_required
def editCategory(request, id):
    #The user will be able to edit the chategory income.
    expensesAmount = Expense.objects.filter(user=request.user)
    totalExpenses = sum(expense.amount for expense in expensesAmount)
    incomesAmount = Income.objects.filter(user=request.user)
    totalIncomes = sum(income.amount for income in incomesAmount)
    balance = totalIncomes - totalExpenses
    category = Category.objects.get(pk=id)
    context = {
        'category': category,
        'values': category,
        'totalExpenses': totalExpenses, 
        'totalIncomes':totalIncomes, 
        'balance':balance,
    }
    if request.method == 'GET':
        return render(request, 'moneymate/categories/edit_category.html', context)
    if request.method == 'POST':
        name = request.POST['name']

        if not name:
            return render(request, 'moneymate/categories/edit_category.html', context)

        category.name = name
        category.save()

        return redirect('listCategories')


@login_required
def deleteCategory(request, id):
    # The user will be able to delete the chosen category.
    category = Category.objects.get(pk=id)
    category.delete()
    return redirect('listCategories')

