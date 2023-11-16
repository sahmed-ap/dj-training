from django.db import models

# Create your models here.

from django.db.models import Model


class Content(Model):
    title = models.CharField(max_length=50, blank=True, null=False)
    publish = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}"
