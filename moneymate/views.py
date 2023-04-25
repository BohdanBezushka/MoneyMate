from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .models import Category, Expense, Origin, Income, Currency
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

@login_required
def dashboard(request):
    # When the user logs in or registers, he/she will be taken 
    # directly to the templates/moneymate/dashboard.html file.

    chosen_currency_id = request.session.get('chosen_currency')
    #Currency chosen by the user. If none is chosen, then the euro will be displayed.
    if chosen_currency_id:
        chosen_currency = Currency.objects.get(pk=chosen_currency_id)
        currency_symbol = chosen_currency.symbol
    else:
        currency_symbol = "€"
    
    expensesAmount = Expense.objects.filter(user=request.user)
    totalExpenses = sum(expense.amount for expense in expensesAmount)
    incomesAmount = Income.objects.filter(user=request.user)
    totalIncomes = sum(income.amount for income in incomesAmount)
    balance = totalIncomes - totalExpenses
    context = {'totalExpenses': totalExpenses, 'totalIncomes':totalIncomes, 'balance':balance, 'currency_symbol': currency_symbol}
    return render(request, 'moneymate/dashboard.html', context)

#                        EXPENSES            ----------

@login_required
def viewExpensesList(request):
    # This feature allows the user to review the expenses
    # they have previously entered in the application. 
    # By clicking on 'Expenses' in the navigation bar of 
    # the dashboard.html, users can access a list of their recorded expenses.

    chosen_currency_id = request.session.get('chosen_currency')
    #Currency chosen by the user. If none is chosen, then the euro will be displayed.
    if chosen_currency_id:
        chosen_currency = Currency.objects.get(pk=chosen_currency_id)
        currency_symbol = chosen_currency.symbol
    else:
        currency_symbol = "€"

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
    context = {'expenses': expenses, 'page_object': page_object, 'totalExpenses': totalExpenses, 'totalIncomes':totalIncomes, 'balance':balance, 'currency_symbol': currency_symbol}
    return render(request, 'moneymate/expenses/list_expenses.html', context)

@login_required
def addExpense(request):
    # This feature enables users to access their expense records.
    # By clicking on the appropriate button

    chosen_currency_id = request.session.get('chosen_currency')
    #Currency chosen by the user. If none is chosen, then the euro will be displayed.
    if chosen_currency_id:
        chosen_currency = Currency.objects.get(pk=chosen_currency_id)
        currency_symbol = chosen_currency.symbol
    else:
        currency_symbol = "€"

    expensesAmount = Expense.objects.filter(user=request.user)
    totalExpenses = sum(expense.amount for expense in expensesAmount)
    incomesAmount = Income.objects.filter(user=request.user)
    totalIncomes = sum(income.amount for income in incomesAmount)
    balance = totalIncomes - totalExpenses
    categories = Category.objects.filter(user=request.user)
    context = {'categories': categories,'values': request.POST, 'totalExpenses': totalExpenses, 'totalIncomes':totalIncomes, 'balance':balance, 'currency_symbol': currency_symbol}
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

@login_required
def editExpense(request, id):
    #The user will be able to edit the chosen expense.

    chosen_currency_id = request.session.get('chosen_currency')
    #Currency chosen by the user. If none is chosen, then the euro will be displayed.
    if chosen_currency_id:
        chosen_currency = Currency.objects.get(pk=chosen_currency_id)
        currency_symbol = chosen_currency.symbol
    else:
        currency_symbol = "€"

    expensesAmount = Expense.objects.filter(user=request.user)
    totalExpenses = sum(expense.amount for expense in expensesAmount)
    incomesAmount = Income.objects.filter(user=request.user)
    totalIncomes = sum(income.amount for income in incomesAmount)
    balance = totalIncomes - totalExpenses
    expense = Expense.objects.get(pk=id)
    categories = Category.objects.filter(user=request.user)
    context = {'expense': expense,'values': expense,'categories': categories, 'totalExpenses': totalExpenses, 'totalIncomes':totalIncomes, 'balance':balance, 'currency_symbol': currency_symbol }
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

@login_required
def deleteExpense(request, id):
    # The user will be able to delete the chosen expense.
    expense = Expense.objects.get(pk=id)
    expense.delete()
    return redirect('listExpenses')


#                        INCOMES           ----------

@login_required
def viewIncomesList(request):
    # This feature allows the user to review the incomes
    # they have previously entered in the application. 
    # By clicking on 'Incomes' in the navigation bar of 
    # the dashboard.html, users can access a list of their recorded incomes.

    chosen_currency_id = request.session.get('chosen_currency')
    #Currency chosen by the user. If none is chosen, then the euro will be displayed.
    if chosen_currency_id:
        chosen_currency = Currency.objects.get(pk=chosen_currency_id)
        currency_symbol = chosen_currency.symbol
    else:
        currency_symbol = "€"

    expensesAmount = Expense.objects.filter(user=request.user)
    totalExpenses = sum(expense.amount for expense in expensesAmount)
    incomesAmount = Income.objects.filter(user=request.user)
    totalIncomes = sum(income.amount for income in incomesAmount)
    balance = totalIncomes - totalExpenses
    origins = Origin.objects.filter(user=request.user)
    incomes = Income.objects.filter(user=request.user).order_by('-date')
    paginate = Paginator(incomes, 3)
    number_of_page = request.GET.get('page')
    page_object = paginate.get_page(number_of_page)
    context = {'incomes': incomes, 'page_object': page_object, 'totalExpenses': totalExpenses, 'totalIncomes':totalIncomes, 'balance':balance, 'currency_symbol': currency_symbol}
    return render(request, 'moneymate/incomes/list_incomes.html', context)

@login_required
def addIncome(request):
    # This feature enables users to access their income records.
    # By clicking on the appropriate button.

    chosen_currency_id = request.session.get('chosen_currency')
    #Currency chosen by the user. If none is chosen, then the euro will be displayed.
    if chosen_currency_id:
        chosen_currency = Currency.objects.get(pk=chosen_currency_id)
        currency_symbol = chosen_currency.symbol
    else:
        currency_symbol = "€"

    expensesAmount = Expense.objects.filter(user=request.user)
    totalExpenses = sum(expense.amount for expense in expensesAmount)
    incomesAmount = Income.objects.filter(user=request.user)
    totalIncomes = sum(income.amount for income in incomesAmount)
    balance = totalIncomes - totalExpenses
    origins = Origin.objects.filter(user=request.user)
    context = {'origins': origins,'values': request.POST, 'totalExpenses': totalExpenses, 'totalIncomes':totalIncomes, 'balance':balance, 'currency_symbol': currency_symbol}
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

@login_required
def editIncome(request, id):
    #The user will be able to edit the chosen income.

    chosen_currency_id = request.session.get('chosen_currency')
    #Currency chosen by the user. If none is chosen, then the euro will be displayed.
    if chosen_currency_id:
        chosen_currency = Currency.objects.get(pk=chosen_currency_id)
        currency_symbol = chosen_currency.symbol
    else:
        currency_symbol = "€"

    expensesAmount = Expense.objects.filter(user=request.user)
    totalExpenses = sum(expense.amount for expense in expensesAmount)
    incomesAmount = Income.objects.filter(user=request.user)
    totalIncomes = sum(income.amount for income in incomesAmount)
    balance = totalIncomes - totalExpenses
    income = Income.objects.get(pk=id)
    origins = Origin.objects.filter(user=request.user)
    context = {
        'income': income,
        'values': income,
        'origins': origins,
        'totalExpenses': totalExpenses, 
        'totalIncomes':totalIncomes, 
        'balance':balance,
        'currency_symbol': currency_symbol,
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

@login_required
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

    chosen_currency_id = request.session.get('chosen_currency')
    #Currency chosen by the user. If none is chosen, then the euro will be displayed.
    if chosen_currency_id:
        chosen_currency = Currency.objects.get(pk=chosen_currency_id)
        currency_symbol = chosen_currency.symbol
    else:
        currency_symbol = "€"

    expensesAmount = Expense.objects.filter(user=request.user)
    totalExpenses = sum(expense.amount for expense in expensesAmount)
    incomesAmount = Income.objects.filter(user=request.user)
    totalIncomes = sum(income.amount for income in incomesAmount)
    balance = totalIncomes - totalExpenses
    categories = Category.objects.filter(user=request.user)
    paginate = Paginator(categories, 3)
    number_of_page = request.GET.get('page')
    page_object = paginate.get_page(number_of_page)
    context = {'categories': categories, 'page_object': page_object, 'totalExpenses': totalExpenses, 'totalIncomes':totalIncomes, 'balance':balance, 'currency_symbol': currency_symbol}
    return render(request, 'moneymate/categories/list_categories.html', context)

@login_required
def addCategory(request):
    # This feature enables users to access their categories.
    # By clicking on the appropriate button.

    chosen_currency_id = request.session.get('chosen_currency')
    #Currency chosen by the user. If none is chosen, then the euro will be displayed.
    if chosen_currency_id:
        chosen_currency = Currency.objects.get(pk=chosen_currency_id)
        currency_symbol = chosen_currency.symbol
    else:
        currency_symbol = "€"

    expensesAmount = Expense.objects.filter(user=request.user)
    totalExpenses = sum(expense.amount for expense in expensesAmount)
    incomesAmount = Income.objects.filter(user=request.user)
    totalIncomes = sum(income.amount for income in incomesAmount)
    balance = totalIncomes - totalExpenses
    categories = Category.objects.filter(user=request.user)
    context = {
        'categories': categories,
        'values': request.POST,
        'totalExpenses': totalExpenses, 
        'totalIncomes':totalIncomes, 
        'balance':balance,
        'currency_symbol': currency_symbol,
    }
    if request.method == 'GET':
        return render(request, 'moneymate/categories/add_category.html', context)

    if request.method == 'POST':
        name = request.POST['name']

        if not name:
            return render(request, 'moneymate/categories/add_category.html', context)

        category = Category(name=name)
        category.user = request.user
        category.save()

        return redirect('listCategories')

@login_required
def editCategory(request, id):
    #The user will be able to edit the chategory income.

    chosen_currency_id = request.session.get('chosen_currency')
    #Currency chosen by the user. If none is chosen, then the euro will be displayed.
    if chosen_currency_id:
        chosen_currency = Currency.objects.get(pk=chosen_currency_id)
        currency_symbol = chosen_currency.symbol
    else:
        currency_symbol = "€"

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
        'currency_symbol': currency_symbol,
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


#                        ORIGINS         ----------
@login_required
def viewOriginsList(request):
    # This feature allows the user to review the origins
    # they have previously entered in the application. 
    # By clicking on 'Origin' in the navigation bar of 
    # the dashboard.html, users can access a list of their recorded origins.

    chosen_currency_id = request.session.get('chosen_currency')
    #Currency chosen by the user. If none is chosen, then the euro will be displayed.
    if chosen_currency_id:
        chosen_currency = Currency.objects.get(pk=chosen_currency_id)
        currency_symbol = chosen_currency.symbol
    else:
        currency_symbol = "€"

    expensesAmount = Expense.objects.filter(user=request.user)
    totalExpenses = sum(expense.amount for expense in expensesAmount)
    incomesAmount = Income.objects.filter(user=request.user)
    totalIncomes = sum(income.amount for income in incomesAmount)
    balance = totalIncomes - totalExpenses
    origins = Origin.objects.filter(user=request.user)
    paginate = Paginator(origins, 3)
    number_of_page = request.GET.get('page')
    page_object = paginate.get_page(number_of_page)
    context = {'origins': origins, 'page_object': page_object, 'totalExpenses': totalExpenses, 'totalIncomes':totalIncomes, 'balance':balance, 'currency_symbol': currency_symbol}
    return render(request, 'moneymate/origins/list_origins.html', context)

@login_required
def addOrigin(request):
    # This feature enables users to access their origins.
    # By clicking on the appropriate button.

    chosen_currency_id = request.session.get('chosen_currency')
    #Currency chosen by the user. If none is chosen, then the euro will be displayed.
    if chosen_currency_id:
        chosen_currency = Currency.objects.get(pk=chosen_currency_id)
        currency_symbol = chosen_currency.symbol
    else:
        currency_symbol = "€"

    expensesAmount = Expense.objects.filter(user=request.user)
    totalExpenses = sum(expense.amount for expense in expensesAmount)
    incomesAmount = Income.objects.filter(user=request.user)
    totalIncomes = sum(income.amount for income in incomesAmount)
    balance = totalIncomes - totalExpenses
    origins = Origin.objects.filter(user=request.user)
    context = {
        'origins': origins,
        'values': request.POST,
        'totalExpenses': totalExpenses, 
        'totalIncomes':totalIncomes, 
        'balance':balance,
        'currency_symbol': currency_symbol,
    }
    if request.method == 'GET':
        return render(request, 'moneymate/origins/add_origin.html', context)

    if request.method == 'POST':
        name = request.POST['name']

        if not name:
            return render(request, 'moneymate/origins/add_origin.html', context)

        origin = Origin(name=name)
        origin.user = request.user
        origin.save()

        return redirect('listOrigins')

@login_required
def editOrigin(request, id):
    #The user will be able to edit origins.

    chosen_currency_id = request.session.get('chosen_currency')
    #Currency chosen by the user. If none is chosen, then the euro will be displayed.
    if chosen_currency_id:
        chosen_currency = Currency.objects.get(pk=chosen_currency_id)
        currency_symbol = chosen_currency.symbol
    else:
        currency_symbol = "€"

    expensesAmount = Expense.objects.filter(user=request.user)
    totalExpenses = sum(expense.amount for expense in expensesAmount)
    incomesAmount = Income.objects.filter(user=request.user)
    totalIncomes = sum(income.amount for income in incomesAmount)
    balance = totalIncomes - totalExpenses
    origin = Origin.objects.get(pk=id)
    context = {
        'origin': origin,
        'values': origin,
        'totalExpenses': totalExpenses, 
        'totalIncomes':totalIncomes, 
        'balance':balance,
        'currency_symbol': currency_symbol,
    }
    if request.method == 'GET':
        return render(request, 'moneymate/origins/edit_origin.html', context)
    if request.method == 'POST':
        name = request.POST['name']

        if not name:
            return render(request, 'moneymate/origins/edit_origin.html', context)

        origin.name = name
        origin.save()

        return redirect('listOrigins')


@login_required
def deleteOrigin(request, id):
    # The user will be able to delete the chosen origin.
    origin = Origin.objects.get(pk=id)
    origin.delete()
    return redirect('listOrigins')

#                          CURRENCIES                   ----------

@login_required
def viewCurrenciesList(request):
    # This feature allows the user to review the currencies
    # they have previously entered in the application. 
    # By clicking on 'Currency' in the navigation bar of 
    # the dashboard.html, users can access a list of their recorded currencies.

    chosen_currency_id = request.session.get('chosen_currency')
    #Currency chosen by the user. If none is chosen, then the euro will be displayed.
    if chosen_currency_id:
        chosen_currency = Currency.objects.get(pk=chosen_currency_id)
        currency_symbol = chosen_currency.symbol
    else:
        currency_symbol = "€"

    currencies = Currency.objects.filter(user=request.user)
    paginate = Paginator(currencies, 3)
    number_of_page = request.GET.get('page')
    page_object = paginate.get_page(number_of_page)
    expensesAmount = Expense.objects.filter(user=request.user)
    totalExpenses = sum(expense.amount for expense in expensesAmount)
    incomesAmount = Income.objects.filter(user=request.user)
    totalIncomes = sum(income.amount for income in incomesAmount)
    balance = totalIncomes - totalExpenses
    context = {'currencies': currencies, 'page_object': page_object, 'totalExpenses': totalExpenses, 'totalIncomes':totalIncomes, 'balance':balance, 'currency_symbol': currency_symbol}
    return render(request, 'moneymate/currencies/list_currencies.html', context)

@login_required
def addCurrency(request):
    # This feature enables users to access their currency records.
    # By clicking on the appropriate button.

    chosen_currency_id = request.session.get('chosen_currency')
    #Currency chosen by the user. If none is chosen, then the euro will be displayed.
    if chosen_currency_id:
        chosen_currency = Currency.objects.get(pk=chosen_currency_id)
        currency_symbol = chosen_currency.symbol
    else:
        currency_symbol = "€"

    expensesAmount = Expense.objects.filter(user=request.user)
    totalExpenses = sum(expense.amount for expense in expensesAmount)
    incomesAmount = Income.objects.filter(user=request.user)
    totalIncomes = sum(income.amount for income in incomesAmount)
    balance = totalIncomes - totalExpenses
    currencies = Currency.objects.filter(user=request.user)
    context = {'currencies': currencies,'values': request.POST, 'totalExpenses': totalExpenses, 'totalIncomes':totalIncomes, 'balance':balance, 'currency_symbol': currency_symbol}
    if request.method == 'GET':
        return render(request, 'moneymate/currencies/add_currency.html', context)

    if request.method == 'POST':
        currency = request.POST['currency']

        if not currency:
            return render(request, 'moneymate/currencies/add_currency.html', context)
        abbreviation = request.POST['abbreviation']
        symbol = request.POST['symbol']

        if not symbol:
            return render(request, 'moneymate/currencies/add_currency.html', context)

        Currency.objects.create(user=request.user, currency=currency, abbreviation=abbreviation, symbol=symbol)

        return redirect('listCurrencies')

@login_required
def editCurrency(request, id):
    #The user will be able to edit the chosen currency.

    chosen_currency_id = request.session.get('chosen_currency')
    #Currency chosen by the user. If none is chosen, then the euro will be displayed.
    if chosen_currency_id:
        chosen_currency = Currency.objects.get(pk=chosen_currency_id)
        currency_symbol = chosen_currency.symbol
    else:
        currency_symbol = "€"

    expensesAmount = Expense.objects.filter(user=request.user)
    totalExpenses = sum(expense.amount for expense in expensesAmount)
    incomesAmount = Income.objects.filter(user=request.user)
    totalIncomes = sum(income.amount for income in incomesAmount)
    balance = totalIncomes - totalExpenses
    currency = Currency.objects.get(pk=id)
    context = {'currency': currency,'values': currency, 'totalExpenses': totalExpenses, 'totalIncomes':totalIncomes, 'balance':balance, 'currency_symbol': currency_symbol }
    if request.method == 'GET':
        return render(request, 'moneymate/currencies/edit_currency.html', context)
    if request.method == 'POST':
        currency_name = request.POST['currency']

        if not currency:
            return render(request, 'moneymate/currencies/edit_currency.html', context)
        abbreviation = request.POST['abbreviation']
        symbol = request.POST['symbol']

        if not abbreviation:
            return render(request, 'moneymate/currencies/edit_currency.html', context)
        currency.user = request.user
        currency.currency = currency_name
        currency.abbreviation = abbreviation
        currency.symbol = symbol

        currency.save()

        return redirect('listCurrencies')


@login_required
def deleteCurrency(request, id):
    # The user will be able to delete the chosen currency.
    currency = Currency.objects.get(pk=id)
    currency.delete()
    return redirect('listCurrencies')

def chooseCurrency(request):
    # The user can choose their preferred currency.
    expensesAmount = Expense.objects.filter(user=request.user)
    totalExpenses = sum(expense.amount for expense in expensesAmount)
    incomesAmount = Income.objects.filter(user=request.user)
    totalIncomes = sum(income.amount for income in incomesAmount)
    balance = totalIncomes - totalExpenses

    if request.method == 'POST':
        currency_id = request.POST.get('currency')
        request.session['chosen_currency'] = currency_id
        currency = Currency.objects.get(pk=currency_id)
        currencies = Currency.objects.filter(user=request.user)
        context = {
            'currency': currency,
            'currencies': currencies,
            'totalExpenses': totalExpenses,
            'totalIncomes': totalIncomes,
            'balance': balance,
            'chosen_currency': currency,
        }
        return render(request, 'moneymate/currencies/choose_currency.html', context)
    else:
        currencies = Currency.objects.filter(user=request.user)
        context = {'currencies': currencies}
        return render(request, 'moneymate/currencies/choose_currency.html', context)
