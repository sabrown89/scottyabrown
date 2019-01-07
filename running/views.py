from django.shortcuts import render
from running.models import RunningDay

def index(request):
    running_days = RunningDay.objects.order_by('day')
    return render(request, 'running/index.html', {'running_days': running_days})
