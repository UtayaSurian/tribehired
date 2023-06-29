from django.urls import path
from . import views

urlpatterns = [
    path('', views.home), # home page to view top posts
    path('api/top_posts/', views.top_posts), # same as home page
    path('api/search/', views.search_comments, name='search_comments'),
]
