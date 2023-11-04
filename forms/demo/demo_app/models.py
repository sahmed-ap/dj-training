from django.db import models


# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=200)
    slugline = models.CharField(max_length=200)
    seo_title = models.CharField(max_length=200)
