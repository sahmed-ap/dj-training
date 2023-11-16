import datetime
import json

from articles.forms import ArticlePostForm
from django.http import HttpResponseRedirect
from django.shortcuts import render


# Create your views here.


def render_article_page(request, article_slug):
    article_data = {
        "title": "Business News",
        "author": "Biden",
        "published": datetime.datetime.now().strftime('%d/%m/%Y, %H:%M:%S'),
        "body": "WASHINGTON (AP) — It was a meeting a year in the making.President Joe Biden and Chinese President Xi Jinping sat down together on Wednesday just outside of San Francisco, where Asian leaders gathered for an annual summit. It was almost exactly one year since their last encounter in Bali, Indonesia, on the sidelines of another global gathering.In addition to a formal bilateral meeting, Biden and Xi shared a lunch with top advisers and strolled the verdant grounds of the luxury estate where their meeting took place."
    }
    return render(request, "index.html", {"article": article_data, "article_slug": article_slug})


def create_article(request):
    if request.method == 'POST':
        form = ArticlePostForm(request.POST)
        if form.is_valid():
            json_file_path = "/Users/salmman.ahmmed/Documents/trainings/newsApp/articles_data.json"
            articles_data = []
            with open(json_file_path, "r") as json_file:
                articles_data = json.load(json_file)
            form_data = {
                'title': form.data.get('title'),
                'author': form.data.get('author'),
                'body': form.data.get('body'),
                'slug': form.data.get('title') + '-' + form.data.get('author'),
                'published': 'today'
            }
            if len(articles_data) > 0:
                articles_data.append(form_data)

            with open(json_file_path, "w") as json_file:
                json.dump(articles_data, json_file, indent=4)
            return HttpResponseRedirect('/')  # Replace with your success URL
    else:
        form = ArticlePostForm()
    return render(request, 'create.html', {'form': form, 'action': 'Create a Article'})


def update_article_instance(list_of_dicts, article_slug, updated_data):
    for item in list_of_dicts:
        if item['slug'] == article_slug:
            item.update(updated_data)
            break


def update_article(request, article_slug):
    articles_data = []
    json_file_path = "/Users/salmman.ahmmed/Documents/trainings/newsApp/articles_data.json"
    with open(json_file_path, "r") as json_file:
        articles_data = json.load(json_file)

    result_article = next(item for item in articles_data if item["slug"] == article_slug)

    if request.method == 'POST':
        form = ArticlePostForm(request.POST)
        if form.is_valid():
            json_file_path = "/Users/salmman.ahmmed/Documents/trainings/newsApp/articles_data.json"
            updated_data = {
                'title': form.data.get('title'),
                'author': form.data.get('author'),
                'body': form.data.get('body'),
                'slug': form.data.get('title') + '-' + form.data.get('author'),
                'published': 'today'
            }
            update_article_instance(articles_data, article_slug, updated_data)

            with open(json_file_path, "w") as json_file:
                json.dump(articles_data, json_file, indent=4)

            return HttpResponseRedirect('/')  # Replace with your success URL
    else:
        form = ArticlePostForm(initial=result_article)
    return render(request, 'create.html', {'form': form, 'action': 'Update a Article'})
