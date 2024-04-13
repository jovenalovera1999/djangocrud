from django import forms
from .models import Gender

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