from django.shortcuts import render
from django.http import HttpResponse
from projects.forms import CalculateAge, CalculateCurrency
from projects.calculators import calculate_age, calculate_currency_DOLLAR_RUB

# Create your views here.

def age_calculator(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        age = request.POST.get("date_birth")
        age = calculate_age(age)
        context = {
            'show_form': False,
            'hi': 'Hello',
            'name': name,
            'date_birth': age
        }
        return render(request, 'projects/age_calculator.html', context)
    else:
        form = CalculateAge()
        context = {
            'show_form': True,
            'hi': 'Hello',
            'form': form
        }
        return render(request, 'projects/age_calculator.html', context)


def calculator_currency(request):
    if request.method == 'POST':
        currency = request.POST.get("currency")
        amount = request.POST.get("amount")
        if currency == 'DOL':
            currency = calculate_currency_DOLLAR_RUB(amount)
            context = {
                'show_form': False,
                'amount': amount,
                'currency': currency,
            }
            return render(request, 'projects/current_dollar.html', context)
    else:
        form = CalculateCurrency()
        context = {
            'show_form': True,
            'form': form
        }
        return render(request, 'projects/current_dollar.html', context)
