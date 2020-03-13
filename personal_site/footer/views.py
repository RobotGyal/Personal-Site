from django.shortcuts import render



def about(request):
    return render(request, 'footer/about.html.html')


def contact(request):
    return render(request, 'footer/contact.html')