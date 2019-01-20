from django.shortcuts import render
from running.models import RunningDay

def index(request):
    rd = RunningDay.objects
    return render(request, 'running/index.html', {
        'running_days': rd.order_by('-day'),
        'mileage_per_day': rd.mileage_per_day(),
        'running_dates': rd.running_dates()
    })
