from django.shortcuts import render


def index(request):
    return render(request, 'static_pages/index.html', {})


def handler404(request, *args, **kwargs):
    return render(request, 'static_pages/404.html', status=404)
