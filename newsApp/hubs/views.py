from django.shortcuts import render


# Create your views here.

def hub_page(request, hub_name):
    """
    return hub page
    """
    return render(request, "hub-page.html", {"hub_name": hub_name})
