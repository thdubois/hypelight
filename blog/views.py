from django.shortcuts import render
from .models import Article, Images
from django.shortcuts import get_list_or_404

# Create your views here.


def articles(request):
    articles = get_list_or_404(Article)
    return render(request, 'blog/articles.html', {'articles': articles})


def index(request):
    article_index = get_list_or_404(Article)
    return render(request, 'blog/index.html', {'articles_index': article_index})


def galerie(request):
    images = get_list_or_404(Images)
    return render(request, 'blog/galerie.html', {'images': images})
