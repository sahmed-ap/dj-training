from articles import views
from django.urls import path

urlpatterns = [
    path("<str:article_slug>", views.render_article_page, name="article-page"),
    path("create/", views.create_article, name="article-page-create"),
    path("update/<str:article_slug>", views.update_article, name="article-page-update"),
]
