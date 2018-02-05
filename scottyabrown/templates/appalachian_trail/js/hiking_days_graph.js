<script>
var ctx_polar = document.getElementById('myPolarChart').getContext('2d');
var chart_polar = new Chart(ctx_polar, {
    // The type of chart we want to create
    type: 'pie',

    // The data for our dataset
    data: {
        labels: ['{{hiking_days|safe}} hiking days',' {{days_off|safe}} days off (zeros)'],
        datasets: [
            {
            data: [
                {{ hiking_days|safe }},
                {{ days_off|safe }}
            ],
            backgroundColor: [
                'rgba(139, 0, 139, .8)',
                 'rgba(0, 255, 127, .4)',
            ],
            borderColor: [
                'rgba(139, 0, 139)',
                'rgba(0, 255, 127)',
            ],
            borderWidth: 1,
            },
        ]
    },

    // Configuration options go here
    options: {
        responsive: false,
        title: {
            display: true,
            fontSize: 16,
            text: 'Hiking Days versus Days Off'
        }
    }
});
</script>
