# dashboard/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.income_expense_graph, name='income_expense_graph'),  # URL for displaying both income and expense graphs
    path('income/', views.income_graph, name='income_graph'),  # URL for the income graph
    path('expense/', views.expense_graph, name='expense_graph'),  # URL for the expense graph
]
