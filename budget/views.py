from django.views.generic import TemplateView
from django.shortcuts import render, redirect, get_object_or_404

from .forms import IncomeForm, ExpenseForm
from .models import Income, Expense


class HomePageView(TemplateView):
    template_name = 'home.html'
    


def budget_view(request):
    incomes = Income.objects.filter(user=request.user)
    expenses = Expense.objects.filter(user=request.user)

    total_income = sum(income.income_amount for income in incomes)
    total_expenses = sum(expense.expense_amount for expense in expenses)
    remaining_balance = total_income - total_expenses
    
    if request.method == 'POST':
        if 'income_submit' in request.POST:
            form = IncomeForm(request.POST)
            if form.is_valid():
                income = form.save(commit=False)
                income.user = request.user
                income.save()
                return redirect('budget')
        elif 'expense_submit' in request.POST:
            form = ExpenseForm(request.POST)
            if form.is_valid():
                expense = form.save(commit=False)
                expense.user = request.user
                expense.save()
                return redirect('budget')
    else:
        income_form = IncomeForm()
        expense_form = ExpenseForm()

    return render(request, 'budget.html', {
        'incomes': incomes,
        'expenses': expenses,
        'income_form': income_form,
        'expense_form': expense_form,
        'total_income': total_income,
        'total_expenses': total_expenses,
        'remaining_balance': remaining_balance,
    })
    
def delete_income(request, income_id):
    income = get_object_or_404(Income, id=income_id)
    if income.user == request.user:
        income.delete()
    return redirect('budget')

def delete_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id)
    if expense.user == request.user:
        expense.delete()
    return redirect('budget')