from django.shortcuts import render


def index(request):
    return render(request, 'public_user/index.html')


def portfolio(request):
    return render(request, 'public_user/portfolio.html')


def howitworks(request):
    return render(request, 'public_user/howitworks.html')
