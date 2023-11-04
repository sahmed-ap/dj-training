from django.contrib import admin
from session3app.models import Article

# Register your models here.


admin.site.register(Article, admin.ModelAdmin)
