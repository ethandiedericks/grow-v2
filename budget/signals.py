from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

from .models import IncomeSource, ExpenseSource, InvestmentSource

# Retrieve the User model
User = get_user_model()

# income source signal

# Define your default sources
default_sources = [
    ('salary', 'Salary'), 
    ('freelance-income', 'Freelance Income'),
    ('investment-returns', 'Investment Returns'),
    ('rental-income', 'Rental Income'),
    ('business-profits', 'Business Profits'),
    ('royalties', 'Royalties'),
    ('social-security-benefits', 'Social Security Benefits'),
    ('pension', 'Pension'),
    ('grands-and-scholarships','Grants and Scholarships'),
    ('alimony-or-child-support','Alimony or Child Support'),
]

default_expenses = [
    ('housing', 'Housing'),
    ('transportation', 'Transportation'),
    ('food', 'Food'),
    ('healthcare', 'Healthcare'),
    ('debt-payments', 'Debt Payments'),
    ('personal-care', 'Personal Care'),
    ('entertainment', 'Entertainment'),
    ('education', 'Education'),
    ('clothing', 'Clothing'),
    ('savings-and-investments', 'Savings and Investments'),
    ('childcare', 'Childcare'),
    ('insurance', 'Insurance'),
]

default_investments = [
    ('stocks', 'Stocks'),
    ('bonds', 'Bonds'),
    ('mutual-funds', 'Mutual Funds'),
    ('exchange-traded-funds', 'Exchange-Traded Funds (ETFs)'),
    ('real-estate', 'Real Estate'),
    ('certificates-of-deposit', 'Certificates of Deposit (CDs)'),
    ('retirement-accounts', 'Retirement Accounts'),
    ('commodities', 'Commodities'),
    ('savings-accounts', 'Savings Accounts'),
    ('cryptocurrencies', 'Cryptocurrencies'),
    ('annuities', 'Annuities'),
]

# Signal receiver function to create default IncomeSource, ExpenseSource, InvestmentSource instances
@receiver(post_save, sender=User)
def create_default_income_sources(sender, instance, created, **kwargs):
    """
    Signal receiver function to create default IncomeSource instances for a new user.
    """
    if created:
        for source in default_sources:
            IncomeSource.objects.create(user=instance, name=source[1])
    
@receiver(post_save, sender=User)
def create_default_expenses(sender, instance, created, **kwargs):
    """
    Signal receiver function to create default ExpenseSource instances for a new user.
    """
    if created:
        for expense in default_expenses:
            ExpenseSource.objects.create(user=instance, name=expense[1])
            

@receiver(post_save, sender=User)
def create_default_investments(sender, instance, created, **kwargs):
    """
    Signal receiver function to create default InvestmentSource instances for a new user.
    """
    if created:
        for investment in default_investments:
            InvestmentSource.objects.create(user=instance, name=investment[1])
            

