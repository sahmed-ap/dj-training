from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),  # /calendar/
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge, name="month-calendar"),
    path("<month>", views.dynamic_monthly_challenge, name="dynamic-months"),
    path("reverse/<int:month>", views.monthly_challenge_by_number_reverse),
    path("http-resp/<int:month>", views.monthly_challenge_http_response),
    path("template-as-string/<int:month>", views.monthly_challenge_render_template),
    path("template-render/<int:month>", views.monthly_challenge_render_view),
    path("month-detail/<int:month>", views.monthly_challenge_template_variable, name="month-detail"),
]
