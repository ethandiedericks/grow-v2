from django.urls import path
from . import views

urlpatterns = [
    path(
        "", views.DashboardView.as_view(), name="dashboard"
    ),  # URL for displaying both income and expense graphs
    path("income_sources/", views.IncomeSourcesView.as_view(), name="income_sources"),
    path(
        "expense_categories/",
        views.ExpenseCategoriesView.as_view(),
        name="expense_categories",
    ),
    path(
        "investment_categories/",
        views.InvestmentCategoriesView.as_view(),
        name="investment_categories",
    ),
    path(
        "bar-line-chart/", views.BarLineChartDataView.as_view(), name="bar_line_chart"
    ),  # URL for bar and line chart data
    path(
        "category-chart/", views.CategoryChartDataView.as_view(), name="category_chart"
    ),  # URL for category chart data
]
