from django.urls import path
from .views import HomePageView, budget_view, delete_income, delete_expense

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('budget/', budget_view, name='budget'),
    path('delete_income/<int:income_id>/', delete_income, name='delete_income'),
    path('delete_expense/<int:expense_id>/', delete_expense, name='delete_expense'),
]