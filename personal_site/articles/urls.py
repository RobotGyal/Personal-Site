
from django.contrib import admin
from django.urls import path
from articles import views as article_views
from articles.views import ArticleDetailView, ArticleMainView

urlpatterns = [
    # path('', article_views.articles),
    path('<str:pk>/', ArticleDetailView.as_view(), name='article-details-page'),
    path('', ArticleMainView.as_view(), name='article-main-page'),
    # path('<str:slug>/', article_views.detail),

    
]
