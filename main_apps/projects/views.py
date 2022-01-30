from django.shortcuts import render
from django.http import HttpResponse
from projects.forms import Calculate_age
from projects.calculators import calculate_age

# Create your views here.

def show_projects(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        age = request.POST.get("age")
        age = calculate_age(age)
        context = {
            'show_form': False,
            'hi': 'Hello',
            'name': name,
            'age': age
        }
        return render(request, 'projects/projects.html', context)
    else:
        form = Calculate_age()
        context = {
            'show_form': True,
            'hi': 'Hello',
            'form': form
        }
        return render(request, 'projects/projects.html', context)

