# Register your models here.
from django.contrib import admin

from articles.models import Article



admin.site.register(Article, admin.ModelAdmin)
