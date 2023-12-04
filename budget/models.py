from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
# Create your models here.
class Income(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    income_name = models.CharField(max_length=150)
    income_amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(default=timezone.now) 
    
    def __str__(self):
        return f"{self.name} - {self.amount}"
    
class Expense(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    expense_name = models.CharField(max_length=150)
    expense_amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(default=timezone.now) 
    
    def __str__(self):
        return f"{self.name} - {self.amount}"