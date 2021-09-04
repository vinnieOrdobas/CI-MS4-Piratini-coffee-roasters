from django.shortcuts import render

# Create your views here.


def view_bag(request):
    """
    Renders the shopping bag view
    """

    return render(request, 'bag/bag.html')
