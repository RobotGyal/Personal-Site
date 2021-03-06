"""personal_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from articles import views as article_views
from websites import views as website_views
from code import views as code_views
from robotics import views as robotics_views
from footer import views as footer_views


urlpatterns = [
    path('', article_views.index),
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
    path('websites/', include('websites.urls')),
    path('code/', code_views.index),
    path('robotics/', robotics_views.index),
    path('about/', footer_views.about),
    path('contact/', footer_views.contact),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
