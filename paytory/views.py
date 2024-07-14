from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import User, Token, Expense, Income
from .forms import ExpenseForm, IncomeForm
from datetime import datetime

@csrf_exempt
def submit_expense(request):
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token=this_token).get()
    if 'date' not in request.POST:
        date = datetime.now()
    else:
        date = request.POST['date']

    Expense.objects.create(user=this_user, amount=request.POST['amount'],
                           text=request.POST['text'], date=date)

    return JsonResponse({'status': 'ok'}, encoder=JSONEncoder)

@csrf_exempt
def submit_income(request):
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token=this_token).get()
    if 'date' not in request.POST:
        date = datetime.now()
    else:
        date = request.POST['date']

    Income.objects.create(user=this_user, amount=request.POST['amount'],
                          text=request.POST['text'], date=date)

    return JsonResponse({'status': 'ok'}, encoder=JSONEncoder)


def home(request):
    # Initialize empty lists
    expenses = []
    incomes = []

    if request.user.is_authenticated:
        expenses = Expense.objects.filter(user=request.user)
        incomes = Income.objects.filter(user=request.user)

    # Handle form submissions
    if request.method == 'POST':
        if 'submit_expense' in request.POST:
            expense_form = ExpenseForm(request.POST)
            if expense_form.is_valid():
                expense = expense_form.save(commit=False)
                expense.user = request.user  # Set the user
                expense.save()
        elif 'submit_income' in request.POST:
            income_form = IncomeForm(request.POST)
            if income_form.is_valid():
                income = income_form.save(commit=False)
                income.user = request.user  # Set the user
                income.save()

    expense_form = ExpenseForm()
    income_form = IncomeForm()

    context = {
        'expenses': expenses,
        'incomes': incomes,
        'expense_form': expense_form,
        'income_form': income_form,
    }
    return render(request, 'home.html', context)


@login_required
def delete_expense(request, id):
    expense = get_object_or_404(Expense, id=id, user=request.user)
    expense.delete()
    return redirect('home')

@login_required
def delete_income(request, id):
    income = get_object_or_404(Income, id=id, user=request.user)
    income.delete()
    return redirect('home')
