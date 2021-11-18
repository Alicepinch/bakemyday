from django.shortcuts import render

# Create your views here.


def index(request):
    """
    View to return index page
    """
    return render(request, 'home/index.html')


def contact_us(request):
    """
    View to return contact us page
    """
    return render(request, 'home/contact-us.html')


def about_us(request):
    """
    View to return about us page
    """
    return render(request, 'home/about-us.html')
