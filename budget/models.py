from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class IncomeSource(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.name
    
class ExpenseSource(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.name
    
class InvestmentSource(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.name
    
    
class Income(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    income_name = models.CharField(max_length=150)
    income_amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateField(auto_now_add=True) 
    future_income_date = models.DateField('Future income date', blank=True, null=True)
    
    def __str__(self):
        return f"{self.income_name} - {self.income_amount}"
    
class Expense(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    expense_name = models.CharField(max_length=150)
    expense_amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateField(auto_now_add=True) 
    future_expense_date = models.DateField('Future expense date', blank=True, null=True)
    
    def __str__(self):
        return f"{self.expense_name} - {self.expense_amount}"
    
class Investment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    investment_name = models.CharField(max_length=150)
    investment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateField(auto_now_add=True) 
    future_investment_date = models.DateField('Future investment date', blank=True, null=True)
    
    def __str__(self):
        return f"{self.investment_name} - {self.investment_amount}"