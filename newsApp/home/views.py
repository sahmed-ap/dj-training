import json

from django.shortcuts import render
from articles.models import Article
from django.contrib.auth.models import User

# Create your views here.

def home_page(request):
    """
    View return home page.
    """
    articles_data = []
    articles = Article.objects.all()
    for result_article in articles:
        article_data = {
            "title": result_article.title,
            "author": result_article.author.username,
            "published": result_article.published.strftime('%d/%m/%Y, %H:%M:%S'),
            "body": result_article.body,
            "slug": result_article.slug
        }
        articles_data.append(article_data)
    return render(request, 'home.html', {'articles': articles_data})
