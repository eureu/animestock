from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.Search.as_view(), name='search'),
    path('genres/', views.genres, name='genres'),
    path('anime/', views.anime, name='anime')
]