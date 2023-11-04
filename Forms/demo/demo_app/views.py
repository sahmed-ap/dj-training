from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .forms import ArticleForm, ArticleModeForm


# Create your views here.
def home_view(request):
    context = {}
    context['form'] = ArticleForm()
    return render(request, "simple_form.html", context)


def model_form_view(request):
    context = {}
    context['form'] = ArticleModeForm()
    return render(request, "model_form.html", context)


def submit_model_form(request):
    form = ArticleModeForm(request.POST)
    if form.is_valid():
        form.save()
    return HttpResponse("Form saved successfully")


def submit_form(request):
    title = request.POST.get("title")
    slugline = request.POST.get("slugline")
    seo_title = request.POST.get("seo_title")
    print("Title", title)
    print("Slugline", slugline)
    print("Seo Title", seo_title)
    return HttpResponse("Got Response successfully")
