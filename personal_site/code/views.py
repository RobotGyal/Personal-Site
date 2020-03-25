from django.shortcuts import render
from .models import Code
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

# Create your views here.
def index(request):

    context={
        'codes': Code.objects.all()
    }
    return render(request, 'code/code_index.html', context)


# class index(ListView):
#     """ Renders a list of all Pages. """
#     model = Code

#     def get(self, request):
#         """ GET a list of Pages. """
#         # articles = self.get_queryset().all()
#         context={
#             'codes': Code.objects.all()
#     }
#         return render(request, '.html', context)