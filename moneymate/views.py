from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm

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

    
