from django.db import models
from django.contrib.auth import get_user_model

class Income(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    income_name = models.CharField(max_length=150)
    income_amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.income_name} - {self.income_amount}"
    
class Expense(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    expense_name = models.CharField(max_length=150)
    expense_amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.expense_name} - {self.expense_amount}"
