import json

from django.shortcuts import render


# Create your views here.

def home_page(request):
    """
    View return home page.
    """
    articles_data = []
    json_file_path = "/Users/salmman.ahmmed/Documents/trainings/newsApp/articles_data.json"
    with open(json_file_path, "r") as json_file:
        articles_data = json.load(json_file)
    return render(request, 'home.html', {'articles': articles_data})
