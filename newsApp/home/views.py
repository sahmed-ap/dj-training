import json

from django.shortcuts import render


# Create your views here.

def home_page(request):
    """
    View return home page.
    """
    articles_data = []
    json_file_path = "D:/Django-Training/articles-example/dj-training/newsApp/articles_data.json"
    with open(json_file_path, "r") as json_file:
        articles_data = json.load(json_file)
    return render(request, 'home.html', {'articles': articles_data})
