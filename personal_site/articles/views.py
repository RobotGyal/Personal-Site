from django.shortcuts import render
from .models import Article

def index(request):
    return render(request, 'base.html')

def articles(request):
    context={
        'articles': Article.objects.all()
    }
    return render(request, 'articles/articles.html', context)