<script>
var ctx_per_day = document.getElementById('myPerDayOrderedChart').getContext('2d');
var chart_per_day = new Chart(ctx_per_day, {
    // The type of chart we want to create
    type: 'bar',

    // The data for our dataset
    data: {
        labels: {{ hiking_dates_by_miles_hiked|safe }},
        datasets: [{
            label: "Miles Hiked Each Day (ordered lowest miles to highest)",
            backgroundColor: 'rgba(255, 99, 132, .8)',
            borderColor: 'rgba(255, 99, 132)',
            borderWidth: 1,
            data: {{ mileage_per_day_by_miles_hiked|safe }},
            }],
    },

    // Configuration options go here
    options: {
        responsive: false,
        title: {
            display: true,
            fontSize: 16,
            text: 'Miles Hiked Each Day Ordered'
        }
    }
});
</script>
