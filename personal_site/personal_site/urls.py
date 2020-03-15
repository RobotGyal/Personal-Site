
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
    path('contact/', include('footer.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
