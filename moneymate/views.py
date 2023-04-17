from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm

# Create your views here:

def homePage(request):
    # This is the main page that will be displayed to the user.
    # The function has been exported to the 'expensesapp' 
    # project in the 'urls.py' file in order to visualize the HTML content.
    return render(request, 'moneymate/base.html')

def login(request):
    #The user can log in.
    form = AuthenticationForm()
    return render(request, 'moneymate/accounts/login.html', {'form': form})

def signup(request):
    #The user can sign up.
    form = AuthenticationForm()
    return render(request, 'moneymate/accounts/signup.html', {'form': form})