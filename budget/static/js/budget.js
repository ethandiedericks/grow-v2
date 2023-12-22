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

// delete cards:

  
        function deleteItem(itemId, itemType) {
            fetch(`/delete_${itemType}/${itemId}`, {
                method: 'DELETE',
                headers: {
                    'X-CSRFToken': '{{ csrf_token }}',
                    'Content-Type': 'application/json'
                }
            })
            .then(response => {
                if (response.ok) {
                    const cardToRemove = document.querySelector(`.card[data-item-id="${itemId}"]`);
                    if (cardToRemove) {
                        cardToRemove.remove();
    
                        // Fetch updated totals after successful deletion
                        fetch('/get_updated_totals/')
                            .then(response => response.json())
                            .then(data => {
                                // Update total income
                                document.getElementById('totalIncome').innerHTML = `<h4 class="h6">Total Income: ${data.total_income}</h4>`;
    
                                // Update total expenses and remaining balance
                                document.getElementById('totalExpenses').innerHTML = `<h4 class="h6">Total Expenses: ${data.total_expenses}</h4><h4 class="h6">Remaining Balance: ${data.remaining_balance}</h4>`;
    
                                // Update total investments
                                document.getElementById('totalInvestments').innerHTML = `<h4 class="h6">Total Investments: ${data.total_investments}</h4>`;
                            })
                            .catch(error => {
                                console.error('Error fetching updated totals:', error);
                            });
                    }
                }
            })
            .catch(error => {
                console.error('Error deleting item:', error);
            });
        }

        function activateTab(tabId) {
        $('#financialTabs a[href="#' + tabId + '"]').tab('show');
    }


