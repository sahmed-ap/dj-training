from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),  # /challenges/
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge, name="month-challenge"),
    path("<month>", views.dynamic_monthly_challenge, name="dynamic_months"),
    path("reverse/<int:month>", views.monthly_challenge_by_number_reverse),
    path("http-resp/<int:month>", views.monthly_challenge_http_response),
]
