from django.urls import path
from .views import HomePageView, BudgetPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('budget/', BudgetPageView.as_view(), name='budget')
]