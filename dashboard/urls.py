from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),  # URL for displaying both income and expense graphs
    path('income_sources/', views.income_sources, name = 'income_souces'),
    path('expense_categories/', views.expense_categories, name = 'expense_categories'),
    path('investment_categories/', views.investment_categories, name = 'investment_categories'),
    path('bar-line-chart/', views.bar_line_chart_data, name='bar_line_chart'),  # URL for bar and line chart data
    path('category-chart/', views.category_chart_data, name='category_chart'),  # URL for category chart data
]
