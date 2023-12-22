from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from .forms import IncomeForm, ExpenseForm, InvestmentForm
from .models import (
    Income,
    Expense,
    Investment,
    IncomeSource,
    ExpenseSource,
    InvestmentSource,
)
from django.views.generic import View, TemplateView
from django.http import HttpResponseNotAllowed


class HomePageView(TemplateView):
    template_name = "home.html"


class BudgetView(LoginRequiredMixin, View):
    template_name = "budget/budget.html"
    income_form_class = IncomeForm
    expense_form_class = ExpenseForm
    investment_form_class = InvestmentForm

    def get_total_amounts(self, user):
        incomes = Income.objects.filter(user=user)
        expenses = Expense.objects.filter(user=user)
        investments = Investment.objects.filter(user=user)

        total_income = sum(income.income_amount for income in incomes)
        total_expenses = sum(expense.expense_amount for expense in expenses)
        total_investments = sum(
            investment.investment_amount for investment in investments
        )

        return (
            total_income,
            total_expenses,
            total_investments,
            incomes,
            expenses,
            investments,
        )

    def get(self, request):
        user = request.user
        (
            total_income,
            total_expenses,
            total_investments,
            incomes,
            expenses,
            investments,
        ) = self.get_total_amounts(user)

        remaining_balance = total_income - total_expenses - total_investments

        income_sources = IncomeSource.objects.filter(user=user)
        income_form = self.income_form_class(user=user)
        income_form.fields["income_name"].queryset = income_sources

        expense_sources = ExpenseSource.objects.filter(user=user)
        expense_form = self.expense_form_class(user=user)
        expense_form.fields["expense_name"].queryset = expense_sources

        investment_sources = InvestmentSource.objects.filter(user=user)
        investment_form = self.investment_form_class(user=user)
        investment_form.fields["investment_name"].queryset = investment_sources

        context = {
            "incomes": incomes,
            "expenses": expenses,
            "investments": investments,
            "income_form": income_form,
            "expense_form": expense_form,
            "investment_form": investment_form,
            "total_income": total_income,
            "total_expenses": total_expenses,
            "total_investments": total_investments,
            "remaining_balance": remaining_balance,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        user = request.user

        if "income_submit" in request.POST:
            income_form = IncomeForm(request.POST, user=user)
            if income_form.is_valid():
                income = income_form.save(commit=False)
                income.user = request.user

                selected_income_source_id = request.POST.get("income_name")
                if selected_income_source_id == "custom":
                    custom_income_name = request.POST.get("custom_income")
                    if custom_income_name:
                        new_income_source = IncomeSource.objects.create(
                            user=user, name=custom_income_name
                        )
                        income.income_name = new_income_source
                else:
                    selected_income_source = get_object_or_404(
                        IncomeSource, id=selected_income_source_id
                    )
                    income.income_name = selected_income_source

                income.save()
                return redirect("budget")

        elif "expense_submit" in request.POST:
            expense_form = ExpenseForm(request.POST, user=user)
            if expense_form.is_valid():
                expense = expense_form.save(commit=False)
                expense.user = request.user

                selected_expense_source_id = request.POST.get("expense_name")
                if selected_expense_source_id == "custom":
                    custom_expense_name = request.POST.get("custom_expense")
                    if custom_expense_name:
                        new_expense_source = ExpenseSource.objects.create(
                            user=user, name=custom_expense_name
                        )
                        expense.expense_name = new_expense_source
                else:
                    selected_expense_source = get_object_or_404(
                        ExpenseSource, id=selected_expense_source_id
                    )
                    expense.expense_name = selected_expense_source

                expense.save()
                return redirect("budget")

        elif "investment_submit" in request.POST:
            investment_form = InvestmentForm(request.POST, user=user)
            if investment_form.is_valid():
                investment = investment_form.save(commit=False)
                investment.user = request.user

                selected_investment_source_id = request.POST.get("investment_name")
                if selected_investment_source_id == "custom":
                    custom_investment_name = request.POST.get("custom_investment")
                    if custom_investment_name:
                        new_investment_source = InvestmentSource.objects.create(
                            user=user, name=custom_investment_name
                        )
                        investment.investment_name = new_investment_source
                else:
                    selected_investment_source = get_object_or_404(
                        InvestmentSource, id=selected_investment_source_id
                    )
                    investment.investment_name = selected_investment_source

                investment.save()
                return redirect("budget")


class DeleteIncomeView(LoginRequiredMixin, View):
    def delete(self, request, income_id):
        income = get_object_or_404(Income, id=income_id)
        if income.user == request.user:
            income.delete()
            return JsonResponse({"message": "Income deleted successfully"})
        else:
            return HttpResponseNotAllowed(["DELETE"])


class DeleteExpenseView(LoginRequiredMixin, View):
    def delete(self, request, expense_id):
        expense = get_object_or_404(Expense, id=expense_id)
        if expense.user == request.user:
            expense.delete()
            return JsonResponse({"message": "Expense deleted successfully"})
        else:
            return HttpResponseNotAllowed(["DELETE"])


class DeleteInvestmentView(LoginRequiredMixin, View):
    def delete(self, request, investment_id):
        investment = get_object_or_404(Investment, id=investment_id)
        if investment.user == request.user:
            investment.delete()
            return JsonResponse({"message": "Investment deleted successfully"})
        else:
            return HttpResponseNotAllowed(["DELETE"])


class GetUpdatedTotalsView(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        incomes = Income.objects.filter(user=user)
        expenses = Expense.objects.filter(user=user)
        investments = Investment.objects.filter(user=user)

        total_income = sum(income.income_amount for income in incomes)
        total_expenses = sum(expense.expense_amount for expense in expenses)
        total_investments = sum(
            investment.investment_amount for investment in investments
        )
        remaining_balance = total_income - total_expenses - total_investments

        return JsonResponse(
            {
                "total_income": total_income,
                "total_expenses": total_expenses,
                "total_investments": total_investments,
                "remaining_balance": remaining_balance,
            }
        )
