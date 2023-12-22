from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.db.models import Sum
from budget.models import (
    Income,
    Expense,
    Investment,
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
        totals = Income.objects.filter(user=request.user).aggregate(
            total_income=Sum("income_amount"),
            total_expense=Sum("expense_amount"),
            total_investment=Sum("investment_amount"),
        )

        labels = ["Total Income", "Total Expense", "Total Investment"]
        values_bar_chart = [
            totals["total_income"] or 0,
            totals["total_expense"] or 0,
            totals["total_investment"] or 0,
        ]
        values_line_chart = values_bar_chart

        return JsonResponse(
            {
                "labels": labels,
                "values_bar_chart": values_bar_chart,
                "values_line_chart": values_line_chart,
            }
        )


class CategoryChartDataView(LoginRequiredMixin, View):
    def get(self, request):
        expense_data = (
            Expense.objects.filter(user=request.user)
            .values("expense_name")
            .annotate(total=Sum("expense_amount"))
        )

        income_data = (
            Income.objects.filter(user=request.user)
            .values("income_name")
            .annotate(total=Sum("income_amount"))
        )

        investment_data = (
            Investment.objects.filter(user=request.user)
            .values("investment_name")
            .annotate(total=Sum("investment_amount"))
        )

        return JsonResponse(
            {
                "expense_labels": [data["expense_name"] for data in expense_data],
                "expense_values": [data["total"] or 0 for data in expense_data],
                "income_labels": [data["income_name"] for data in income_data],
                "income_values": [data["total"] or 0 for data in income_data],
                "investment_labels": [
                    data["investment_name"] for data in investment_data
                ],
                "investment_values": [data["total"] or 0 for data in investment_data],
            }
        )


class IncomeSourcesView(LoginRequiredMixin, View):
    def get(self, request):
        income_data = (
            Income.objects.filter(user=request.user)
            .values("income_name")
            .annotate(total=Sum("income_amount"))
        )

        return JsonResponse(
            {
                "labels": [data["income_name"] for data in income_data],
                "values": [data["total"] or 0 for data in income_data],
            }
        )


class ExpenseCategoriesView(LoginRequiredMixin, View):
    def get(self, request):
        expense_data = (
            Expense.objects.filter(user=request.user)
            .values("expense_name")
            .annotate(total=Sum("expense_amount"))
        )

        return JsonResponse(
            {
                "labels": [data["expense_name"] for data in expense_data],
                "values": [data["total"] or 0 for data in expense_data],
            }
        )


class InvestmentCategoriesView(LoginRequiredMixin, View):
    def get(self, request):
        investment_data = (
            Investment.objects.filter(user=request.user)
            .values("investment_name")
            .annotate(total=Sum("investment_amount"))
        )

        return JsonResponse(
            {
                "labels": [data["investment_name"] for data in investment_data],
                "values": [data["total"] or 0 for data in investment_data],
            }
        )
