from django.shortcuts import render
from django.http import JsonResponse
from json import JSONEncoder
from django.views.decorators.csrf import csrf_exempt
from .models import User, Token, Expense, Income
from datetime import datetime

# Create your views here.
@csrf_exempt
def submit_expense(request):
    """User submits an expense"""

    #TODO: validate data. User might be fake. Token might be fake. Amount might be...
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token=this_token).get()
    if not 'date' in request.POST:
        date = datetime.now() #TODO: User might want to submit the date heself/herself

    Expense.objects.create(user=this_user, amount=request.POST['amount'],
            text=request.POST['text'], date=date)

    return JsonResponse({
        'status': 'ok',
    }, encoder=JSONEncoder)

@csrf_exempt
def submit_income(request):
    """User submits an expense"""

    #TODO: validate data. User might be fake. Token might be fake. Amount might be...
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token=this_token).get()
    if not 'date' in request.POST:
        date = datetime.now() #TODO: User might want to submit the date himself/herself
    Income.objects.create(user=this_user, amount=request.POST['amount'],
            text=request.POST['text'], date=date)

    return JsonResponse({
        'status': 'ok',
    }, encoder=JSONEncoder)
