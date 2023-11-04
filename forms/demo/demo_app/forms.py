# import the standard Django forms
# from built-in library 
from django import forms
from django.forms import ModelForm
from session3app.models import Article


# creating a form 
class ArticleForm(forms.Form):
    title = forms.CharField(max_length=200)
    slugline = forms.CharField(max_length=200)
    seo_title = forms.CharField(
        help_text="Enter title for SEO"
    )


class ArticleModeForm(ModelForm):
    class Meta:
        model = Article
        fields = ["title", "slugline", "seo_title"]
