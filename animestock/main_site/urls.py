from django.urls import path
from . import views
# from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.Search.as_view(), name='search'),
    path('genres/', views.genres, name='genres'),
    path('anime/', views.anime, name='anime'),
    path('genres/<slug:slug>/', views.AnimeDetail.as_view(), name='page_anime'),
    path('register', views.registerPage, name='register'),
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('favourites', views.fav, name='favourites'),
]
#  genres/<slug:slug>/
# url(r'^genres/<slug:slug>/<int:_id>', views.AnimeDetail, name='page_anime'),