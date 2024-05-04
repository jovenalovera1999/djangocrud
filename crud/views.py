from django.shortcuts import render, redirect
from .models import Gender, User
from .forms import GenderForm, GenderFormReadOnly, UserForm
from django.contrib import messages

# Create your views here.

def list_genders(request):
    genders = Gender.objects.all()
    context = {
        'genders': genders,
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
        return redirect('/genders')
    
def view_gender(request, id):
    gender = Gender.objects.get(pk=id)
    form = GenderFormReadOnly(instance=gender)

    context = {
        'form': form,
    }

    return render(request, 'gender/view.html', context)

def edit_gender(request, id):
    gender = Gender.objects.get(pk=id)
    form = GenderForm(instance=gender)

    context = {
        'gender': gender,
        'form': form,
    }

    return render(request, 'gender/edit.html', context)

def update_gender(request, id):
    gender = Gender.objects.get(pk=id)
    form = GenderForm(request.POST, instance=gender)

    if form.is_valid():
        form.save()
        messages.success(request, 'Gender successfully updated.')
        return redirect('/genders')
    
def delete_gender(request, id):
    gender = Gender.objects.get(pk=id)
    form = GenderFormReadOnly(instance=gender)

    context = {
        'gender': gender,
        'form': form,
    }

    return render(request, 'gender/delete.html', context)

def destroy_gender(request, id):
    gender = Gender.objects.get(pk=id)
    gender.delete()
    messages.success(request, 'Gender successfully deleted.')
    return redirect('/genders')

def list_users(request):
    users = User.objects.select_related('gender').all()
    context = {
        'users': users,
    }

    return render(request, 'user/list.html', context)

def add_user(request):
    form = UserForm()
    context = {
        'form': form,
    }
    return render(request, 'user/add.html', context)

def store_user(request):
    form = UserForm(request.POST)

    if form.is_valid():
        form.save()
        messages.success(request, 'User successfully saved.')
        return redirect('/users')