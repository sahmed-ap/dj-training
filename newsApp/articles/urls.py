from articles import views
from django.urls import path

urlpatterns = [
    path("signup", views.signup_view, name="signup"),
    path("signup-user", views.complete_signup, name="complete-signup"),
    path("login", views.login_view, name="login"),
    path("login-user", views.complete_login, name="complete-login"),
    path("create", views.create_article, name="article-page-create"),
    path("my-articles", views.view_my_articles, name="my-articles"),
    path("update/<str:article_slug>", views.update_article, name="article-page-update"),
    path("delete/<str:article_slug>", views.update_delete, name="article-page-delete"),
    path("<str:article_slug>", views.render_article_page, name="article-page"),
    
]
