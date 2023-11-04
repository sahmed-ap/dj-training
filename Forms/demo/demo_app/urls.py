from django.urls import path
from session3app import views

urlpatterns = [
    path("/submit_form", views.submit_form),
    path("/submit_model_form", views.submit_model_form),
    path("/simple_form", views.home_view),
    path("/model_form", views.model_form_view),
]
