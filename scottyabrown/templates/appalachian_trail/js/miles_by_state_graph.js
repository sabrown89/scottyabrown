<script>
var ctx = document.getElementById('myStateChart').getContext('2d');
var chart = new Chart(ctx, {
    // The type of chart we want to create
    type: 'bar',

    // The data for our dataset
    data: {
        labels: {{ states_list|safe }},
        datasets: [{
            label: "Days Spent in Each State",
            backgroundColor: 'rgba(255, 99, 132, .2)',
            borderColor: 'rgba(255, 99, 132)',
            borderWidth: 1,
            data: {{ hiking_days_per_state|safe }},
            },
            {
            label: "Days of Precipitation in Each State",
            backgroundColor: 'rgba(173, 216, 230, .9)',
            borderColor: 'rgba(173, 216, 230)',
            borderWdith: 1,
            data: {{ precipitation_days_per_state|safe }},
        }],
   //     ],
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
            text: 'Days Spent in Each State with Precipitation'
        }
    }
});
</script>
