from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponseForbidden, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import User, Token, Expense, Income, Score
from .forms import ExpenseForm, IncomeForm
from datetime import datetime
from json import JSONEncoder
import uuid

@csrf_exempt
def submit_expense(request):
    try:
        this_token = request.POST['token']
        this_user = User.objects.filter(token__token=this_token).get()
        if 'date' not in request.POST:
            date = datetime.now()
        else:
            date = request.POST['date']

        expense = Expense.objects.create(
            user=this_user,
            amount=request.POST['amount'],
            text=request.POST['text'],
            date=date
        )
    except User.DoesNotExist:
        return JsonResponse({'status': '403 Forbidden'}, encoder=JSONEncoder)

    return JsonResponse({'status': 'ok'}, encoder=JSONEncoder)

@csrf_exempt
def submit_income(request):
    try:
        this_token = request.POST['token']
        this_user = User.objects.filter(token__token=this_token).get()
        if 'date' not in request.POST:
            date = datetime.now()
        else:
            date = request.POST['date']

        income = Income.objects.create(
            user=this_user,
            amount=request.POST['amount'],
            text=request.POST['text'],
            date=date
        )
        return JsonResponse({'status': 'ok'}, encoder=JSONEncoder)
    except User.DoesNotExist:
        return JsonResponse({'status': '403 Forbidden'}, encoder=JSONEncoder)


@login_required
def reset_score(request):
    user_score = get_object_or_404(Score, user=request.user)
    user_score.score = 0
    user_score.save()
    return redirect('home')


def home(request):
    # Initialize empty lists
    expenses = []
    incomes = []

    if request.user.is_authenticated:
        expenses = Expense.objects.filter(user=request.user)
        incomes = Income.objects.filter(user=request.user)
        user_score, _ = Score.objects.get_or_create(user=request.user)
        score = user_score.score

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

@login_required
def confirm_developer(request):
    if request.method == "POST":
        request.session['is_developer'] = True
        return redirect('devoptions')
    return render(request, 'devoptions_enable.html')

@login_required
def dev_options(request):
    is_developer = request.session.get('is_developer', False)
    return render(request, 'devoptions.html', {'is_developer': is_developer})

@login_required
@login_required
def disable_developer(request):
    if request.method == "POST":
        request.session['is_developer'] = False
        return redirect('home')
    return redirect('home')


@login_required
def generate_token(request):
    if not request.session.get('is_developer'):
        return HttpResponseForbidden("You are not authorized to generate tokens.")
    new_token = uuid.uuid4().hex
    Token.objects.create(user=request.user, token=new_token)
    return render(request, 'show_token.html', {'token': new_token})

@login_required
def manage_tokens(request):
    if not request.session.get('is_developer'):
        return HttpResponseForbidden("You are not authorized to manage tokens.")
    tokens = Token.objects.filter(user=request.user)
    return render(request, 'manage_tokens.html', {'tokens': tokens})

@login_required
def revoke_token(request, token_id):
    if not request.session.get('is_developer'):
        return HttpResponseForbidden("You are not authorized to revoke tokens.")
    token = get_object_or_404(Token, id=token_id, user=request.user)
    token.delete()
    return redirect('manage_tokens')
