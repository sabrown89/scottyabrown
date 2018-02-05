<script>
var ctx_per_day = document.getElementById('myPerDayChart').getContext('2d');
var mpd = {{ mileage_per_day|safe }};
var mpd_ga = mpd.slice(0,8);
var mpd_nc = mpd.slice(8,34);
var mpd_tn = mpd.slice(34,42);
var mpd_va = mpd.slice(42,86);
var mpd_wv = mpd.slice(86,89);
var mpd_md = mpd.slice(89,92);
var mpd_pa = mpd.slice(92,110);
var mpd_nj = mpd.slice(110,116);
var mpd_ny = mpd.slice(116,123);
var mpd_ct = mpd.slice(123,126);
var mpd_ma = mpd.slice(126,135);
var mpd_vt = mpd.slice(135,145);
var mpd_nh = mpd.slice(145,161);
var mpd_me = mpd.slice(161,178);

var chart_per_day = new Chart(ctx_per_day, {
    // The type of chart we want to create
    type: 'bar',

    // The data for our dataset
    data: {
        labels: {{ hiking_dates|safe }},
        datasets: [
        {
            label: "GA",
            backgroundColor: 'rgba(209, 0, 0, .6)',
            borderColor: 'rgba(209, 0, 0)',
            borderWidth: 1,
            data: mpd_ga.concat(Array(8)),
        },
        {
            label: "NC",
            backgroundColor: 'rgba(255, 102, 34, .6)',
            borderColor: 'rgba(255, 102, 34)',
            borderWidth: 1,
            data: Array(8).concat(mpd_nc),
         },
         {
            label: "TN",
            backgroundColor: 'rgba(255, 218, 33, .6)',
            borderColor: 'rgba(255, 218, 33)',
            borderWidth: 1,
            data: Array(34).concat(mpd_tn),
         },
         {
            label: "VA",
            backgroundColor: 'rgba(51, 221, 0, .6)',
            borderColor: 'rgba(51, 221, 0)',
            borderWidth: 1,
            data: Array(42).concat(mpd_va),
         },
         {
            label: "WV",
            backgroundColor: 'rgba(17, 51, 204, .6)',
            borderColor: 'rgba(17, 51, 204)',
            borderWidth: 1,
            data: Array(86).concat(mpd_wv),
         },
         {
            label: "MD",
            backgroundColor: 'rgba(34, 0, 102, .6)',
            borderColor: 'rgba(34, 0, 102)',
            borderWidth: 1,
            data: Array(89).concat(mpd_md),
         },
         {
            label: "PA",
            backgroundColor: 'rgba(51, 0, 68, .6)',
            borderColor: 'rgba(51, 0, 68)',
            borderWidth: 1,
            data: Array(92).concat(mpd_pa),
         },
         {
            label: "NJ",
            backgroundColor: 'rgba(220, 20, 60, .6)',
            borderColor: 'rgba(220, 20, 60)',
            borderWidth: 1,
            data: Array(110).concat(mpd_nj),
         },
         {
            label: "NY",
            backgroundColor: 'rgba(255, 140, 0, .6)',
            borderColor: 'rgba(255, 140, 0)',
            borderWidth: 1,
            data: Array(116).concat(mpd_ny),
         },
         {
            label: "CT",
            backgroundColor: 'rgba(255, 255, 102, .6)',
            borderColor: 'rgba(255, 255, 102)',
            borderWidth: 1,
            data: Array(123).concat(mpd_ct),
         },
         {
            label: "MA",
            backgroundColor: 'rgba(46, 139, 87, .6)',
            borderColor: 'rgba(46, 139, 87)',
            borderWidth: 1,
            data: Array(126).concat(mpd_ma),
         },
         {
            label: "VT",
            backgroundColor: 'rgba(0, 191, 255, .6)',
            borderColor: 'rgba(0, 191, 255)',
            borderWidth: 1,
            data: Array(135).concat(mpd_vt),
         },
         {
            label: "NH",
            backgroundColor: 'rgba(106, 90, 205, .6)',
            borderColor: 'rgba(106, 90, 205)',
            borderWidth: 1,
            data: Array(145).concat(mpd_nh),
         },
         {
            label: "ME",
            backgroundColor: 'rgba(138, 43, 226, .6)',
            borderColor: 'rgba(138, 43, 226)',
            borderWidth: 1,
            data: Array(161).concat(mpd_me),
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
            text: 'Miles Hiked Each Day by State',
        }
    }
});
</script>
