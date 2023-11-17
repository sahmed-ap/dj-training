import datetime
import json

from articles.forms import ArticlePostForm, SigunupForm, LoginForm
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from articles.models import Article
# Create your views here.


def render_article_page(request, article_slug):
    articles = Article.objects.filter(author=User.objects.filter(username=request.user.username).first())

    result_article = next(item for item in articles if item.slug == article_slug)
    article_data = {
        "title": result_article.title,
        "author": result_article.author.username,
        "published": result_article.published.strftime('%d/%m/%Y, %H:%M:%S'),
        "body": result_article.body
    }
    return render(request, "index.html", {"article": article_data, "article_slug": article_slug})


def create_article(request):
    if request.method == 'POST':
        form = ArticlePostForm(request.POST)
        if form.is_valid():
            author = User.objects.filter(username=request.user.username).first()
            if author:
                article = Article(author=author, title=form.data.get('title'), body=form.data.get('body'),  published=datetime.datetime.now(), slug=form.data.get('title') + '-' + request.user.username)
                article.save()            
            return HttpResponseRedirect('/')  # Replace with your success URL
    else:
        form = ArticlePostForm()
    if request.user.is_authenticated:
        return render(request, 'create.html', {'form': form, 'action': 'Create a Article'})
    else:
        return HttpResponseRedirect('/')

def view_my_articles(request):
    all_articles = []
    author = User.objects.filter(username=request.user.username).first()
    if author:
        articles = Article.objects.filter(author=author)
        for article in articles:
            all_articles.append({"title": article.title, "body": article.body, "slug": article.slug, "published": article.published})
    return render(request, 'my_articles.html', {'articles': all_articles})   

def update_article_instance(list_of_dicts, article_slug, updated_data):
    for item in list_of_dicts:
        if item['slug'] == article_slug:
            item.update(updated_data)
            break


def update_article(request, article_slug):
    articles = Article.objects.filter(author=User.objects.filter(username=request.user.username).first())

    result_article = next(item for item in articles if item.slug == article_slug)
    if request.method == 'POST':
        form = ArticlePostForm(request.POST)
        if form.is_valid():
            result_article.title = form.data.get('title')
            result_article.body = form.data.get('body')
            result_article.save()
            return HttpResponseRedirect('/article/my-articles') 
    else:
        form = ArticlePostForm(initial={"slug": result_article.slug,
        "title":  result_article.title,
        "published": result_article.published,
        "body":  result_article.body,
        "author": request.user.username,
        })
    return render(request, 'create.html', {'form': form, 'action': 'Update a Article'})


def update_delete(request, article_slug):
    articles = Article.objects.filter(author=User.objects.filter(username=request.user.username).first())
    result_article = next(item for item in articles if item.slug == article_slug)
    result_article.delete()
    return HttpResponseRedirect('/article/my-articles') 


def signup_view(request):
    form = SigunupForm()
    return render(request, 'signup.html', {'form': form})

def complete_signup(request):
    form = SigunupForm(request.POST)
    if form.is_valid():
        user = User.objects.filter(username=request.POST.get("username")).first() 
        if not user: 
            user = User.objects.filter(email=request.POST.get("email")).first() 
        if user:
            return HttpResponse(status=400)
        user = User(username = request.POST.get("username"), email = request.POST.get("email"))
        user.set_password(request.POST.get("password"))
        user.save()
        login(request)
        return HttpResponseRedirect('/') 
    

def login_view(request):
    form = LoginForm()
    return render(request, 'login.html', {'form': form})

def complete_login(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            print("username", username, "password", password)
            # Use the authenticate method to check if the user's credentials are valid
            user = authenticate(request, username=username, password=password)

            if user is not None:
                # If the user is valid, log them in
                login(request, user)
                messages.success(request, 'Login successful!')
                print("Login successful")
                return HttpResponseRedirect('/')  # Redirect to the home page or any other page you want
            else:
                # If the user is not valid, show an error message
                messages.error(request, 'Invalid login credentials.')

        return render(request, 'login.html', {'form': form})