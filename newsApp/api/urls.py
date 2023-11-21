
from django.urls import path
from api import views

urlpatterns = [
    path('articles/', views.article_list, name='article-list'),
    path('articles/<slug:slug>/', views.article_detail, name='article-detail'),
]
