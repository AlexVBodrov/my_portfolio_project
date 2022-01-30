from django.shortcuts import render
from portfolio.models import Portfolio

# Create your views here.


def show_portfolio(request):
    projects = Portfolio.objects.all()
    context = {'projects': projects}
    return render(request, 'portfolio/portfolio.html', context)
