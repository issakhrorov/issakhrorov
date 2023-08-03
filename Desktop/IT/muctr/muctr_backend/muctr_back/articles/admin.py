from django.contrib import admin
from .models import Article, Course, Widget, News

# Register your models here.
admin.site.register((Article, Course, Widget, News))
