from django.shortcuts import render

# Create your views here.


def index(request):
    """
    Renders the home page view
    """

    return render(request, 'home/index.html')
