from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Sum
from budget.models import Income, Expense

def dashboard(request):
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

    #calculate totals
    total_income = incomes.aggregate(total=Sum('income_amount'))['total'] or 0
    total_expense = expenses.aggregate(total=Sum('expense_amount'))['total'] or 0

    # format totals
    formatted_total_income = "{:,.2f}".format(total_income)
    formatted_total_expense = "{:,.2f}".format(total_expense)
    
    return render(request, 'dashboard.html', {
        'incomes': incomes,
        'expenses': expenses,
        'income_data': income_data,
        'expense_data': expense_data,
        'total_income': formatted_total_income,
        'total_expense': formatted_total_expense,
    })

def income_graph(request):
    incomes = Income.objects.filter(user=request.user)
    expenses = Expense.objects.filter(user=request.user)

    # Income data
    income_data = {
        'labels': [income.income_name for income in incomes],
        'values': [income.income_amount for income in incomes],
    }

    # Expense data
    expense_data = {
        'labels': [expense.expense_name for expense in expenses],
        'values': [expense.expense_amount for expense in expenses],
    }

    return JsonResponse({'income_data': income_data, 'expense_data': expense_data})


def expense_graph(request):
    expenses = Expense.objects.filter(user=request.user)

    # Expense data for the line chart
    expense_data = {
        'labels': [expense.expense_name for expense in expenses],
        'values': [expense.expense_amount for expense in expenses],
    }

    return JsonResponse(expense_data)
