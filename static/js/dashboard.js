document.addEventListener('DOMContentLoaded', function() {
    fetch('/dashboard/income/')
        .then(response => response.json())
        .then(data => {
            var incomeData = data.income_data || {};
            var expenseData = data.expense_data || {};

            console.log('Income Data:', incomeData);
            console.log('Expense Data:', expenseData);

            var allLabels = incomeData.labels.concat(expenseData.labels);
            var allValues = incomeData.values.concat(expenseData.values);

            var colors = generateVibrantColors(allLabels.length);

            var ctx1 = document.getElementById('incomeVsExpenseChart').getContext('2d');
            var myChart1 = new Chart(ctx1, {
                type: 'pie',
                data: {
                    labels: allLabels,
                    datasets: [{
                        data: allValues,
                        backgroundColor: colors.backgroundColor,
                        borderColor: colors.borderColor,
                        borderWidth: 1
                    }]
                },
                options: {
                    // Add options here if needed
                }
            });

        });


    fetch('/dashboard/expense/')
        .then(response => response.json())
        .then(data => {
            var ctx2 = document.getElementById('expenseChart').getContext('2d');

            var expenseChart = new Chart(ctx2, {
                type: 'bar',
                data: {
                    labels: data.labels,
                    datasets: [{
                        label: 'Expenses',
                        data: data.values,
                        backgroundColor: 'rgba(255, 99, 132, 0.5)',
                        borderColor: 'rgba(255, 99, 132, 1)',
                        borderWidth: 1
                    }]
                },
                options: {
                    scales: {
                        y: {
                            beginAtZero: true,
                            title: {
                                display: true,
                                text: 'Expense Amount'
                            }
                        }
                    }
                }
            });

        
        });
});

function generateVibrantColors(count) {
    var colors = [];
    var baseColor = chroma.random(); // Generate a random base color

    for (var i = 0; i < count; i++) {
        var vibrantColor = baseColor
            .set('hsl.h', (baseColor.get('hsl.h') + i * 60) % 360) // Adjust hue for each color
            .saturate(2) // Increase saturation for vibrant colors
            .brighten(1); // Increase brightness for vibrant colors

        colors.push(vibrantColor.hex());
    }

    return {
        backgroundColor: colors.map(color => color + '7F'), // Adjust alpha value for transparency
        borderColor: colors
    };
}
