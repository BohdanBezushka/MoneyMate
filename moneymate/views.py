from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .models import Category, Expense
from django.contrib import messages
from django.db.models import Sum
from django.core.paginator import Paginator

# Create your views here:

def homePage(request):
    # This is the main page that will be displayed to the user.
    # The function has been exported to the 'expensesapp' 
    # project in the 'urls.py' file in order to visualize the HTML content.
    return render(request, 'moneymate/base.html')

def dashboard(request):
    # When the user logs in or registers, he/she will be taken 
    # directly to the templates/moneymate/dashboard.html file.
    return render(request, 'moneymate/dashboard.html')

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
    context = {'expenses': expenses, 'page_object': page_object}
    return render(request, 'moneymate/expenses/list_expenses.html', context)

def addExpense(request):
    # This feature enables users to access their expense records.
    # By clicking on the appropriate button
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'values': request.POST
    }
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
    expense = Expense.objects.get(pk=id)
    categories = Category.objects.all()
    context = {
        'expense': expense,
        'values': expense,
        'categories': categories
    }
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
    origins = Origin.objects.all()
    incomes = Income.objects.filter(user=request.user).order_by('-date')
    paginate = Paginator(incomes, 3)
    number_of_page = request.GET.get('page')
    page_object = paginate.get_page(number_of_page)
    context = {'incomes': incomes, 'page_object': page_object}
    return render(request, 'moneymate/incomes/list_incomes.html', context)

def addIncome(request):
    # This feature enables users to access their income records.
    # By clicking on the appropriate button.
    origins = Origin.objects.all()
    context = {
        'origins': origins,
        'values': request.POST
    }
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
    income = Income.objects.get(pk=id)
    origins = origins.objects.all()
    context = {
        'income': income,
        'values': income,
        'origins': origins
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


#           Bug********
def expense_list(request):
    # The user can see the sum of all their expenses on the screen
    expenses = Expense.objects.get(user=request.user)
    total_expenses = expenses.aggregate(Sum('amount'))['amount__sum'] or 0
    context = {
        'expenses': expenses,
        'total_expenses': total_expenses,
    }
    return render(request, 'moneymate/dashboard.html', context)

