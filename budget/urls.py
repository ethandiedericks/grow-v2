from django.urls import path
from .views import HomePageView, budget_view, delete_income, delete_expense, delete_investment,get_updated_totals

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('budget/', budget_view, name='budget'),
    path('delete_income/<int:income_id>/', delete_income, name='delete_income'),
    path('delete_expense/<int:expense_id>/', delete_expense, name='delete_expense'),
    path('delete_investment/<int:investment_id>/', delete_investment, name='delete_investment'),
    path('get_updated_totals/', get_updated_totals, name='get_updated_totals'),
]