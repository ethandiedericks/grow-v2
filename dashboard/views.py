# dashboard/views.py
from django.shortcuts import render
from django.http import JsonResponse
from budget.models import Income, Expense

def income_expense_graph(request):
    # Fetch data for both income and expense graphs for the logged-in user
    incomes = Income.objects.filter(user=request.user)
    expenses = Expense.objects.filter(user=request.user)

    income_data = {
        'labels': [income.income_name for income in incomes],
        'income_values': [income.income_amount for income in incomes],
    }

    expense_data = {
        'labels': [expense.expense_name for expense in expenses],
        'expense_values': [expense.expense_amount for expense in expenses],
    }

    return render(request, 'income_expense_graph.html', {
        'income_data': income_data,
        'expense_data': expense_data
    })

def income_graph(request):
    incomes = Income.objects.filter(user=request.user)
    income_data = {
        'labels': [income.income_name for income in incomes],
        'values': [income.income_amount for income in incomes],
    }
    return JsonResponse(income_data)

def expense_graph(request):
    expenses = Expense.objects.filter(user=request.user)
    expense_data = {
        'labels': [expense.expense_name for expense in expenses],
        'values': [expense.expense_amount for expense in expenses],
    }
    return JsonResponse(expense_data)
