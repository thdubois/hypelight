from django.contrib import admin

# Register your models here.
from blog.models import Article, Images

admin.site.register(Article)
admin.site.register(Images)