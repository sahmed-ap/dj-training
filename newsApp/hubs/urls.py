from django.urls import path
from hubs import views

urlpatterns = [
    path("<str:hub_name>/", views.hub_page, name="hub_page"),
    # path("r/", views.hub_page, name="hub_page"), # ?the=113&admin=amdin-1
]
