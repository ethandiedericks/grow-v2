from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.db.models import Sum
from budget.models import (
    Income,
    Expense,
    Investment,
    IncomeSource,
    ExpenseSource,
    InvestmentSource,
)
from django.views.generic import View


class DashboardView(LoginRequiredMixin, View):
    def get(self, request):
        incomes = Income.objects.filter(user=request.user)
        expenses = Expense.objects.filter(user=request.user)
        investments = Investment.objects.filter(user=request.user)

        income_data = {
            "labels": [income.income_name for income in incomes],
            "income_values": [income.income_amount for income in incomes],
        }

        expense_data = {
            "labels": [expense.expense_name for expense in expenses],
            "expense_values": [expense.expense_amount for expense in expenses],
        }

        investment_data = {
            "labels": [investment.investment_name for investment in investments],
            "values": [investment.investment_amount for investment in investments],
        }

        total_income = incomes.aggregate(total=Sum("income_amount"))["total"] or 0
        total_expense = expenses.aggregate(total=Sum("expense_amount"))["total"] or 0
        total_investment = (
            investments.aggregate(total=Sum("investment_amount"))["total"] or 0
        )

        formatted_total_income = "{:,.2f}".format(total_income)
        formatted_total_expense = "{:,.2f}".format(total_expense)
        formatted_total_investment = "{:,.2f}".format(total_investment)

        return render(
            request,
            "dashboard/dashboard.html",
            {
                "incomes": incomes,
                "expenses": expenses,
                "investments": investments,
                "income_data": income_data,
                "expense_data": expense_data,
                "investment_data": investment_data,
                "total_income": formatted_total_income,
                "total_expense": formatted_total_expense,
                "total_investment": formatted_total_investment,
            },
        )


class BarLineChartDataView(LoginRequiredMixin, View):
    def get(self, request):
        incomes = Income.objects.filter(user=request.user)
        expenses = Expense.objects.filter(user=request.user)
        investments = Investment.objects.filter(user=request.user)

        total_income = incomes.aggregate(total=Sum("income_amount"))["total"] or 0
        total_expense = expenses.aggregate(total=Sum("expense_amount"))["total"] or 0
        total_investment = (
            investments.aggregate(total=Sum("investment_amount"))["total"] or 0
        )

        labels = ["Total Income", "Total Expense", "Total Investment"]
        values_bar_chart = [total_income, total_expense, total_investment]
        values_line_chart = [total_income, total_expense, total_investment]

        return JsonResponse(
            {
                "labels": labels,
                "values_bar_chart": values_bar_chart,
                "values_line_chart": values_line_chart,
            }
        )


class CategoryChartDataView(LoginRequiredMixin, View):
    def get(self, request):
        income_sources = IncomeSource.objects.filter(user=request.user)
        expense_sources = ExpenseSource.objects.filter(user=request.user)
        investment_sources = InvestmentSource.objects.filter(user=request.user)

        expense_data = {
            source.name: Expense.objects.filter(
                user=request.user, expense_name=source.name
            ).aggregate(total=Sum("expense_amount"))["total"]
            or 0
            for source in expense_sources
        }

        income_data = {
            source.name: Income.objects.filter(
                user=request.user, income_name=source.name
            ).aggregate(total=Sum("income_amount"))["total"]
            or 0
            for source in income_sources
        }

        investment_data = {
            source.name: Investment.objects.filter(
                user=request.user, investment_name=source.name
            ).aggregate(total=Sum("investment_amount"))["total"]
            or 0
            for source in investment_sources
        }

        return JsonResponse(
            {
                "expense_labels": list(expense_data.keys()),
                "expense_values": list(expense_data.values()),
                "income_labels": list(income_data.keys()),
                "income_values": list(income_data.values()),
                "investment_labels": list(investment_data.keys()),
                "investment_values": list(investment_data.values()),
            }
        )


class IncomeSourcesView(LoginRequiredMixin, View):
    def get(self, request):
        income_sources = IncomeSource.objects.filter(user=request.user)

        income_data = {
            source.name: Income.objects.filter(
                user=request.user, income_name=source.name
            ).aggregate(total=Sum("income_amount"))["total"]
            or 0
            for source in income_sources
        }

        data = {
            "labels": list(income_data.keys()),
            "values": list(income_data.values()),
        }
        return JsonResponse(data)


class ExpenseCategoriesView(LoginRequiredMixin, View):
    def get(self, request):
        expense_sources = ExpenseSource.objects.filter(user=request.user)

        expense_data = {
            source.name: Expense.objects.filter(
                user=request.user, expense_name=source.name
            ).aggregate(total=Sum("expense_amount"))["total"]
            or 0
            for source in expense_sources
        }

        data = {
            "labels": list(expense_data.keys()),
            "values": list(expense_data.values()),
        }
        return JsonResponse(data)


class InvestmentCategoriesView(LoginRequiredMixin, View):
    def get(self, request):
        investment_sources = InvestmentSource.objects.filter(user=request.user)

        investment_data = {
            source.name: Investment.objects.filter(
                user=request.user, investment_name=source.name
            ).aggregate(total=Sum("investment_amount"))["total"]
            or 0
            for source in investment_sources
        }

        data = {
            "labels": list(investment_data.keys()),
            "values": list(investment_data.values()),
        }
        return JsonResponse(data)
