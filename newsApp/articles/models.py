# Create your models here.
from django.db import models
from django.contrib.auth.models import User
class Article(models.Model):
    title = models.CharField(max_length=100)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    published=models.DateTimeField()
    body=models.TextField()
    slug=models.CharField(max_length=100, null=True, blank=True)