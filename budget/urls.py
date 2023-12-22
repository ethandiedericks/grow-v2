from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("budget/", views.BudgetView.as_view(), name="budget"),
    path(
        "delete_income/<int:income_id>/",
        views.DeleteIncomeView.as_view(),
        name="delete_income",
    ),
    path(
        "delete_expense/<int:expense_id>/",
        views.DeleteExpenseView.as_view(),
        name="delete_expense",
    ),
    path(
        "delete_investment/<int:investment_id>/",
        views.DeleteInvestmentView.as_view(),
        name="delete_investment",
    ),
    path(
        "get_updated_totals/",
        views.GetUpdatedTotalsView.as_view(),
        name="get_updated_totals",
    ),
]
