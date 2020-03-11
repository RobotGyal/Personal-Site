from django.shortcuts import render

def index(request):
    return render(request, 'base.html')

def articles(request):
    return render(request, 'articles/articles.html')