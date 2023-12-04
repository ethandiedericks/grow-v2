from django.contrib import admin
from .models import Income, Expense

@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('user', 'income_name', 'income_amount', 'date_created')
    search_fields = ('income_name',)
    list_filter = ('user',)

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('user', 'expense_name', 'expense_amount', 'date_created')
    search_fields = ('expense_name',)
    list_filter = ('user',)
