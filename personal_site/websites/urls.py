
from django.contrib import admin
from django.urls import path
from websites import views as website_views
from websites.views import WebsiteMainView

urlpatterns = [
    path('', WebsiteMainView.as_view(), name='website-main-page'),    
]
