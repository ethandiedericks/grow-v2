document.addEventListener('DOMContentLoaded', function() {
    // Get the dropdown element
    var incomeTypeDropdown = document.getElementById('id_income_name');
    
    // Get the custom income group element
    var customIncomeGroup = document.querySelector('.custom-income-group');
    
    // Hide the custom income group initially
    customIncomeGroup.classList.add('d-none');
    
    // Add change event listener to the dropdown
    incomeTypeDropdown.addEventListener('change', function() {
        var selectedValue = this.value;
        
        // Check if "Add Custom Income" option is selected
        if (selectedValue === 'custom') {
            // Show the custom income group
            customIncomeGroup.classList.remove('d-none');
        } else {
            // Hide the custom income group
            customIncomeGroup.classList.add('d-none');
        }
    });


});

document.addEventListener('DOMContentLoaded', function() {
    // Get the dropdown element for expenses
    var expenseTypeDropdown = document.getElementById('id_expense_name');
    
    // Get the custom expense group element
    var customExpenseGroup = document.querySelector('.custom-expense-group');
    
    // Hide the custom expense group initially
    customExpenseGroup.classList.add('d-none');
    
    // Add change event listener to the dropdown
    expenseTypeDropdown.addEventListener('change', function() {
        var selectedValue = this.value;
        
        // Check if "Add Custom Expense" option is selected
        if (selectedValue === 'custom') {
            // Show the custom expense group
            customExpenseGroup.classList.remove('d-none');
        } else {
            // Hide the custom expense group
            customExpenseGroup.classList.add('d-none');
        }
    });
});

document.addEventListener('DOMContentLoaded', function() {
    // Get the dropdown element for investments
    var investmentTypeDropdown = document.getElementById('id_investment_name');
    
    // Get the custom investment group element
    var customInvestmentGroup = document.querySelector('.custom-investment-group');
    
    // Hide the custom investment group initially
    customInvestmentGroup.classList.add('d-none');
    
    // Add change event listener to the dropdown
    investmentTypeDropdown.addEventListener('change', function() {
        var selectedValue = this.value;
        
        // Check if "Add Custom Investment" option is selected
        if (selectedValue === 'custom') {
            // Show the custom investment group
            customInvestmentGroup.classList.remove('d-none');
        } else {
            // Hide the custom investment group
            customInvestmentGroup.classList.add('d-none');
        }
    });
});