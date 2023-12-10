from django import forms
from .models import Expense, Income, Investment, IncomeSource, ExpenseSource, InvestmentSource

class IncomeForm(forms.ModelForm):
    """
    Form for handling income data.
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes the IncomeForm instance.
        """
        user = kwargs.pop('user', None)
        super(IncomeForm, self).__init__(*args, **kwargs)
        
        income_sources = IncomeSource.objects.filter(user=user)
        choices = [(source.id, source.name) for source in income_sources]
        choices.append(('custom', 'Add Custom Income'))  # Add the custom option
        
        self.fields['income_name'] = forms.ChoiceField(choices=choices)
        
        # Additional field for custom income
        self.fields['custom_income'] = forms.CharField(
            label='Custom Income', required=False)  # Make it optional

    class Meta:
        model = Income
        fields = ['income_name', 'income_amount', 'future_income_date']
        widgets = {
            'future_income_date': forms.DateInput(attrs={'type': 'date'}),
            'income_name': forms.Select(),
        }

class ExpenseForm(forms.ModelForm):
    """
    Form for handling expense data.
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes the ExpenseForm instance.
        """
        user = kwargs.pop('user', None)
        super(ExpenseForm, self).__init__(*args, **kwargs)
        
        expense_sources = ExpenseSource.objects.filter(user=user)
        choices = [(source.id, source.name) for source in expense_sources]
        choices.append(('custom', 'Add Custom Expense'))  # Add the custom option
        
        self.fields['expense_name'] = forms.ChoiceField(choices=choices)
        
        # Additional field for custom expense
        self.fields['custom_expense'] = forms.CharField(
            label='Custom Expense', required=False)  # Make it optional
        
    class Meta:
        model = Expense
        fields = ['expense_name', 'expense_amount', 'future_expense_date']
        widgets = {
            'future_expense_date': forms.DateInput(attrs={'type': 'date'}),
            'expense_name': forms.Select(),
        }

class InvestmentForm(forms.ModelForm):
    """
    Form for handling investment data.
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes the InvestmentForm instance.
        """
        user = kwargs.pop('user', None)
        super(InvestmentForm, self).__init__(*args, **kwargs)
        
        investment_sources = InvestmentSource.objects.filter(user=user)
        choices = [(source.id, source.name) for source in investment_sources]
        choices.append(('custom', 'Add Custom Investment'))  # Add the custom option
        
        self.fields['investment_name'] = forms.ChoiceField(choices=choices)
        
        # Additional field for custom investment
        self.fields['custom_investment'] = forms.CharField(
            label='Custom Investment', required=False)  # Make it optional
    class Meta:
        model = Investment
        fields = ['investment_name', 'investment_amount', 'future_investment_date']
        widgets = {
            'future_investment_date': forms.DateInput(attrs={'type': 'date'}),
            'investment_name': forms.Select(),
        }
