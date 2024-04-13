from django.shortcuts import render, redirect
from .models import Gender
from .forms import GenderForm, GenderFormReadOnly
from django.contrib import messages

# Create your views here.

def list_genders(request):
    genders = Gender.objects.all()

    context = {
        'genders':genders,
    }

    return render(request, 'gender/list.html', context)

def add_gender(request):
    form = GenderForm()

    context = {
        'form': form,
    }

    return render(request, 'gender/add.html', context)

def store_gender(request):
    form = GenderForm(request.POST)

    if form.is_valid():
        form.save()
        messages.success(request, 'Gender successfully saved.')
        return redirect('list_genders')
    
def view_gender(request, id):
    gender = Gender.objects.get(pk=id)
    form = GenderFormReadOnly(instance=gender)

    context = {
        'form': form,
    }

    return render(request, 'gender/view.html', context)
