from django.shortcuts import render


def dashboard_view(request):
    """
    Main view
    """
    context = {}
    return render(request, 'home/home.html', context)
