from django import forms
from .models import Expense, Income

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['text', 'date', 'amount']

class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['text', 'date', 'amount']
