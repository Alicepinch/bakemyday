from django.shortcuts import render


def index(request):
    """
    View to return index page
    """
    return render(request, 'home/index.html')


def about_us(request):
    """
    View to return about us page
    """
    return render(request, 'home/about-us.html')
