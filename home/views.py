from django.shortcuts import render

# Create your views here.


def index(request):
    """
    Renders the home page view
    """

    return render(request, 'home/index.html')


def about(request):
    """
    Renders the about page view
    """

    return render(request, 'home/about.html')
