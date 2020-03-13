from django.shortcuts import render
from .models import Website
from django.views.generic.list import ListView


# Create your views here.
def index (request):
    return render(request,'websites/website_index.html')

class WebsiteMainView(ListView):
    """ Renders a list of all Pages. """
    model = Website

    def get(self, request):
        """ GET a list of Pages. """
        # articles = self.get_queryset().all()
        context={
            'websites': Website.objects.all()
    }
        return render(request, 'websites/website_index.html', context)