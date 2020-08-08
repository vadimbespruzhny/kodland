from django.urls import path
from my_blog import views

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='main'),
    path('add_article', views.ArticleCreateView.as_view(), name='add_article'),
    path('article_detail/<int:pk>',
         views.ArticleDetailView.as_view(),
         name='article_detail'),
]
