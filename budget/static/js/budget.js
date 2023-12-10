document.addEventListener('DOMContentLoaded', function() {
    var incomeTypeDropdown = document.getElementById('id_income_name');
    var customIncomeGroup = document.querySelector('.custom-income-group');

    if (incomeTypeDropdown && customIncomeGroup) {
        customIncomeGroup.classList.add('d-none');
        
        incomeTypeDropdown.addEventListener('change', function() {
            var selectedValue = this.value;
            
            if (selectedValue === 'custom') {
                customIncomeGroup.classList.remove('d-none');
            } else {
                customIncomeGroup.classList.add('d-none');
            }
        });
    }
});

document.addEventListener('DOMContentLoaded', function() {
    var expenseTypeDropdown = document.getElementById('id_expense_name');
    var customExpenseGroup = document.querySelector('.custom-expense-group');

    if (expenseTypeDropdown && customExpenseGroup) {
        customExpenseGroup.classList.add('d-none');
        
        expenseTypeDropdown.addEventListener('change', function() {
            var selectedValue = this.value;
            
            if (selectedValue === 'custom') {
                customExpenseGroup.classList.remove('d-none');
            } else {
                customExpenseGroup.classList.add('d-none');
            }
        });
    }
});

document.addEventListener('DOMContentLoaded', function() {
    var investmentTypeDropdown = document.getElementById('id_investment_name');
    var customInvestmentGroup = document.querySelector('.custom-investment-group');

    if (investmentTypeDropdown && customInvestmentGroup) {
        customInvestmentGroup.classList.add('d-none');
        
        investmentTypeDropdown.addEventListener('change', function() {
            var selectedValue = this.value;
            
            if (selectedValue === 'custom') {
                customInvestmentGroup.classList.remove('d-none');
            } else {
                customInvestmentGroup.classList.add('d-none');
            }
        });
    } 
});


