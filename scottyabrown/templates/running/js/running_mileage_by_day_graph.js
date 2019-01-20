<script>
var ctx_per_day = document.getElementById('myPerDayChart').getContext('2d');
var mpd = {{ mileage_per_day|safe }};

var chart_per_day = new Chart(ctx_per_day, {
    // The type of chart we want to create
    type: 'bar',

    // The data for our dataset
    data: {
        labels: {{ running_dates|safe }},
        datasets: [
        {
            label: "mileage",
            backgroundColor: 'rgba(209, 0, 0, .6)',
            borderColor: 'rgba(209, 0, 0)',
            borderWidth: 1,
            data: mpd,
        }
         ],
    },

    // Configuration options go here
    options: {
        responsive: false,
        scales: {
            xAxes: [{
                stacked: true,
            }],
        },
        title: {
            display: true,
            fontSize: 16,
            text: 'Mileage Run by Day',
        }
    }
});
</script>
