

function renderBarChart(labels, values, canvasId, chartLabel) {
    console.log('Bar Chart Data:', labels, values);
    var ctx = document.getElementById(canvasId).getContext('2d');

    if (ctx) {
        if (window[canvasId] instanceof Chart) {
            window[canvasId].destroy();
        }

        window[canvasId] = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: labels,
                datasets: [{
                    label: chartLabel,
                    data: values.map(value => parseFloat(value)), // Ensure values are converted to numbers
                    backgroundColor: 'rgba(54, 162, 235, 0.5)',
                    borderColor: 'rgba(54, 162, 235, 1)',
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    y: {
                        beginAtZero: true // Ensure y-axis starts at 0
                    }
                }
            }
        });
    } else {
        console.error('Canvas context not found for', canvasId);
    }
}



function renderLineChart(labels, values, canvasId, chartLabel) {
    console.log('Line Chart Data:', labels, values);
    var ctx = document.getElementById(canvasId).getContext('2d');

    if (window[canvasId] instanceof Chart) {
        window[canvasId].destroy();
    }

    window[canvasId] = new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
                label: chartLabel,
                data: values,
                fill: false,
                borderColor: 'rgba(255, 99, 132, 1)', // Example border color
                borderWidth: 2
            }]
        },
        options: {
            // Add additional options if needed
            responsive: true,
            maintainAspectRatio: false,
        }
    });
}

function renderPieOrDoughnutChart(labels, values, canvasId, chartType) {
    console.log(chartType + ' Chart Data:', labels, values);
    var ctx = document.getElementById(canvasId).getContext('2d');
    
    // Filter out labels with corresponding values equal to 0 or not present
    const filteredLabels = labels.filter((_, index) => parseFloat(values[index]) !== 0);
    const filteredValues = values.filter(value => parseFloat(value) !== 0);

    var chartConfig = {
        type: chartType,
        data: {
            labels: filteredLabels,
            datasets: [{
                label: 'Data',
                data: filteredValues,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.5)',
                    'rgba(54, 162, 235, 0.5)',
                    'rgba(255, 206, 86, 0.5)',
                    // Add more colors as needed
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    // Add more colors as needed
                ],
                borderWidth: 1
            }]
           
        }, 
        options: {
            responsive: true,
            maintainAspectRatio: false,
        },
};

    if (window[canvasId] instanceof Chart) {
        window[canvasId].destroy();
    }

    window[canvasId] = new Chart(ctx, chartConfig);
}

document.addEventListener('DOMContentLoaded', function() {
        const chartSelection = document.getElementById('chartSelection');
        const barChartSection = document.getElementById('barChartSection');
        const lineChartSection = document.getElementById('lineChartSection');
        const pieChartsRow = document.getElementById('pieChartsRow');
        const doughnutChartsRow = document.getElementById('doughnutChartsRow');
    
        if (chartSelection && barChartSection && lineChartSection && pieChartsRow && doughnutChartsRow) {
            chartSelection.addEventListener('change', function () {
                // Hide all chart sections
                [barChartSection, lineChartSection, pieChartsRow, doughnutChartsRow].forEach(section => {
                    section.style.display = 'none';
                });
    
                // Determine which chart section to display based on the selected value
                let selectedChartSection;
                if (chartSelection.value === 'bar') {
                    selectedChartSection = barChartSection;
                } else if (chartSelection.value === 'line') {
                    selectedChartSection = lineChartSection;
                } else if (chartSelection.value === 'pie') {
                    selectedChartSection = pieChartsRow;
                } else if (chartSelection.value === 'doughnut') {
                    selectedChartSection = doughnutChartsRow;
                }
    
                // Update the logic for handling the display of pie and doughnut charts
                if (selectedChartSection === pieChartsRow || selectedChartSection === doughnutChartsRow) {
                    selectedChartSection.style.display = 'flex'; // Show the chart section
                } else {
                    selectedChartSection.style.display = 'block'; // Show the chart section
                }
    
            // Fetch data and render the selected chart
            if (chartSelection.value === 'bar') {
                fetchDataAndRenderBarCharts('/dashboard/income_sources/', 'incomeSourcesBarChart', 'Income Sources');
                fetchDataAndRenderBarCharts('/dashboard/expense_categories/', 'expenseCategoriesBarChart', 'Expense Categories');
                fetchDataAndRenderBarCharts('/dashboard/investment_categories/', 'investmentCategoriesBarChart', 'Investment Categories');
            } else if (chartSelection.value === 'line') {
                fetchDataAndRenderLineCharts('/dashboard/income_sources/', 'incomeSourcesLineChart', 'Income Sources');
                fetchDataAndRenderLineCharts('/dashboard/expense_categories/', 'expenseCategoriesLineChart', 'Expense Categories');
                fetchDataAndRenderLineCharts('/dashboard/investment_categories/', 'investmentCategoriesLineChart', 'Investment Categories');
            } else if (chartSelection.value === 'pie') {
                fetchDataAndRenderPieCharts('/dashboard/category-chart/');
            } else if (chartSelection.value === 'doughnut') {
                fetchDataAndRenderDoughnutCharts('/dashboard/category-chart/');
            }
        });
    
        // Fetch and render the bar charts for income sources, expense categories, and investment categories on page load
        fetchDataAndRenderBarCharts('/dashboard/income_sources/', 'incomeSourcesBarChart', 'Income Sources');
        fetchDataAndRenderBarCharts('/dashboard/expense_categories/', 'expenseCategoriesBarChart', 'Expense Categories');
        fetchDataAndRenderBarCharts('/dashboard/investment_categories/', 'investmentCategoriesBarChart', 'Investment Categories');
    }
    
});
function fetchDataAndRenderLineCharts(url, canvasId, chartLabel) {
    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            console.log('Fetched data for', chartLabel, data); // Log the fetched data

            if (data.labels && data.values) {
                // Filter out labels and values where the value is 0
                const filteredLabels = data.labels.filter((_, index) => parseFloat(data.values[index]) !== 0);
                const filteredValues = data.values.filter(value => parseFloat(value) !== 0);

                renderLineChart(filteredLabels, filteredValues, canvasId, chartLabel);
            } else {
                console.error('Incomplete data for line chart');
            }
        })
        .catch(error => {
            console.error('There was a problem fetching the data or rendering the chart:', error);
        });
}



function fetchDataAndRenderPieCharts(url) {

    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            if (data.expense_labels && data.expense_values) {
                renderPieOrDoughnutChart(data.expense_labels, data.expense_values, 'expensesPieChart', 'pie');
                renderPieOrDoughnutChart(data.income_labels, data.income_values, 'incomeSourcesPieChart', 'pie');
                renderPieOrDoughnutChart(data.investment_labels, data.investment_values, 'investmentPieChart', 'pie');
            } else {
                console.error('Incomplete data for pie charts');
            }
        })
        .catch(error => {
            console.error('There was a problem fetching the data or rendering the pie charts:', error);
        });
}

function fetchDataAndRenderDoughnutCharts(url) {
    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            if (data.expense_labels && data.expense_values) {
                renderPieOrDoughnutChart(data.expense_labels, data.expense_values, 'expensesDoughnutChart', 'doughnut');
                renderPieOrDoughnutChart(data.income_labels, data.income_values, 'incomeSourcesDoughnutChart', 'doughnut');
                renderPieOrDoughnutChart(data.investment_labels, data.investment_values, 'investmentsDoughnutChart', 'doughnut');
            } else {
                console.error('Incomplete data for doughnut charts');
            }
        })
        .catch(error => {
            console.error('There was a problem fetching the data or rendering the doughnut charts:', error);
        });
}

function fetchDataAndRenderBarCharts(url, canvasId, chartLabel) {
    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            console.log('Fetched data for', chartLabel, data); // Log the fetched data

            if (data.labels && data.values) {
                // Filter out labels and values where the value is 0
                const filteredLabels = data.labels.filter((_, index) => parseFloat(data.values[index]) !== 0);
                const filteredValues = data.values.filter(value => parseFloat(value) !== 0);

                renderBarChart(filteredLabels, filteredValues, canvasId, chartLabel);
            } else {
                console.error('Incomplete data for bar chart');
            }
        })
        .catch(error => {
            console.error('There was a problem fetching the data or rendering the chart:', error);
        });
}

