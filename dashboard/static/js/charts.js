function renderBarChart(labels, values) {
    console.log('Bar Chart Data:', labels, values);
    var ctx = document.getElementById('barChart').getContext('2d');

    if (window.barChart instanceof Chart) {
        window.barChart.destroy();
    }

    window.barChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Bar Chart',
                data: values,
                backgroundColor: 'rgba(54, 162, 235, 0.5)', // Example color
                borderColor: 'rgba(54, 162, 235, 1)', // Example border color
                borderWidth: 1
            }]
        },
        options: {
            // Add additional options if needed
            responsive: true,
            maintainAspectRatio: false,
        }
    });
}

function renderLineChart(labels, values) {
    console.log('Line Chart Data:', labels, values);
    var ctx = document.getElementById('lineChart').getContext('2d');

    if (window.lineChart instanceof Chart) {
        window.lineChart.destroy();
    }

    window.lineChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
                label: 'Line Chart',
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
                // Add styling or customization options here
            }]
        }, 
        options: {
            responsive: true,
            maintainAspectRatio: false,
        }
        // Add additional options if needed
    };

    if (window[canvasId] instanceof Chart) {
        window[canvasId].destroy();
    }

    window[canvasId] = new Chart(ctx, chartConfig);
}

document.addEventListener('DOMContentLoaded', function() {
    const chartSelection = document.getElementById('chartSelection');
    const chartSection = document.getElementById('chartSection');

    if (chartSelection && chartSection) {
        
        function fetchDataAndRenderChart(url, chartType) {
            fetch(url)
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    return response.json();
                })
                .then(data => {
                    if (chartType === 'bar') {
                        if (data.labels && data.values_bar_chart) {
                            renderBarChart(data.labels, data.values_bar_chart);
                        } else {
                            console.error('Incomplete data for bar chart');
                        }
                    } else if (chartType === 'line') {
                        if (data.labels && data.values_line_chart) {
                            renderLineChart(data.labels, data.values_line_chart);
                        } else {
                            console.error('Incomplete data for line chart');
                        }
                    } else if (chartType === 'pie') {
                        fetchDataAndRenderPieCharts('/dashboard/category-chart/');
                    } else if (chartType === 'doughnut') {
                        fetchDataAndRenderDoughnutCharts('/dashboard/category-chart/');
                    }
                    // Add conditions for other chart types similarly
                })
                .catch(error => {
                    console.error('There was a problem fetching the data or rendering the chart:', error);
                });
        }

        chartSelection.addEventListener('change', function () {
            chartSection.childNodes.forEach(child => {
                if (child.nodeType === 1) {
                    child.style.display = 'none';
                }
            });

            let selectedChartId;
            if (chartSelection.value === 'bar') {
                selectedChartId = 'barChartSection';
            } else if (chartSelection.value === 'line') {
                selectedChartId = 'lineChartSection';
            } else if (chartSelection.value === 'pie') {
                selectedChartId = 'pieChartsRow';
            } else if (chartSelection.value === 'doughnut') {
                selectedChartId = 'doughnutChartsRow';
            }

            if (selectedChartId) {
                document.getElementById(selectedChartId).style.display = 'block';
            }

            // Fetch data and render the selected chart
            if (chartSelection.value === 'bar' || chartSelection.value === 'line') {
                fetchDataAndRenderChart('/dashboard/bar-line-chart/', chartSelection.value);
            } else if (chartSelection.value === 'pie') {
                fetchDataAndRenderPieCharts('/dashboard/category-chart/');
            } else if (chartSelection.value === 'doughnut') {
                fetchDataAndRenderDoughnutCharts('/dashboard/category-chart/');
            }
        });

        // Set the default chart to display on page load
        fetchDataAndRenderChart('/dashboard/bar-line-chart/', 'bar');
        document.getElementById('barChartSection').style.display = 'block';
    } 
});

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
                renderPieOrDoughnutChart(data.investment_labels, data.investment_values, 'investmentDoughnutChart', 'doughnut');
            } else {
                console.error('Incomplete data for doughnut charts');
            }
        })
        .catch(error => {
            console.error('There was a problem fetching the data or rendering the doughnut charts:', error);
        });
}