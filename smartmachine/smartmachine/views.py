from django.shortcuts import render
from app_machine.models import Station


def dashboard_view(request):
    """
    Main view
    """
    stations = Station.objects.all()
    stats = []

    for st in stations:
        stats.append({st, st.status.last()})


    context = {
        'stations': stations,
        'stats': stats,
    }
    return render(request, 'home/home.html', context)
