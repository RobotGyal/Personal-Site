from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import Article
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView



def index(request):
    return render(request, 'index.html')



# def articles(request):
#     context={
#         'articles': Article.objects.all()
#     }
#     return render(request, 'articles/articles.html', context)



class ArticleMainView(ListView):
    """ Renders a list of all Pages. """
    model = Article

    def get(self, request):
        """ GET a list of Pages. """
        # articles = self.get_queryset().all()
        context={
            'articles': Article.objects.all()
    }
        return render(request, 'articles/articles.html', context)


class ArticleDetailView(DetailView):
    """ Renders a specific page based on it's slug."""
    model = Article