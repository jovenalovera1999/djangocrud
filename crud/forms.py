from django import forms
from .models import Gender, User

class GenderForm(forms.ModelForm):
    class Meta:
        model = Gender
        fields = [
            'gender',
        ]
        widgets = {
            'gender': forms.TextInput(attrs={'class': 'form-control'}),
        }

class GenderFormReadOnly(forms.ModelForm):
    class Meta:
        model = Gender
        fields = [
            'gender',
        ]
        widgets = {
            'gender': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'middle_name',
            'last_name',
            'age',
            'gender',
            'birth_date',
            'contact_number',
            'email_address',
            'username',
            'password',
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'type':'date'}),
            'contact_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email_address': forms.EmailInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }