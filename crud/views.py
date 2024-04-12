from django.shortcuts import render
from .forms import GenderForm

# Create your views here.

def list_genders(request):
    return render(request, 'gender/list.html')

def add_gender(request):
    form = GenderForm()

    context = {
        'form': form
    }

    return render(request, 'gender/add.html', context)