from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from .models import Anime, Genre
from django.db.models import Q
# Create your views here.

def index(request):

    search_query = request.GET.get("q")
    if search_query:
        pass

    return render(request, 'index.html')


def genres(request):
    anime = Anime.objects.all()
    context = {
        'anime' : anime,
    }

    return render(request, 'genres.html', context=context)


def anime(request):
    return render(request, 'anime.html')



class Search(ListView):

    model = Anime
    template_name = 'anime_list.html'
 
    def get_queryset(self): # новый
        query = self.request.GET.get('q')
        if query:
            object_list = Anime.objects.filter(
                Q(title__icontains=query)
            )
        else:
            object_list = Anime.objects.all()
        return object_list


class GenreYear:
    def get_genre(self):
        return Genre.objects.all()


    def get_year(self): 
        return Anime.objects.all()


class Genre(GenreYear):
    def genres(request):
        anime = Anime.objects.all().order_by('id')
        context = {
            'anime_info':anime
        }
        return render(request, 'main/genres.html', context)


class AnimeDetail(GenreYear, DetailView):
    model = Anime
    template_name = 'main/layout_for_anime.html'
    context_object_name = 'anime_page'
    def get(self, request, slug):
        anime = Anime.objects.get(url=slug)
        return render(request, 'main/layout_for_anime.html', {'anime_page' : anime})



# class Search(ListView):

    
#     def get_queryset(self):
#         return Anime.objects.filter(title__icontains=self.request.GET.get("q"))
#         # def get_queryset(self,):
#         # return Movie.objects.filter(name__iregex=self.request.GET.get("q")) исправление проблемы регистра


#     # def get_context_data(self, *args, **kwargs):
#     #     template_name = 'main_site/anime_list.html'
#     #     context = super().get_context_data(*args, **kwargs)
#     #     context["q"] = self.request.GET.get("q")
#     #     return render(request=self.request, template_name=template_name, context=context)    


#     def get_context_data(self, *args, **kwargs):
#         template_name = 'main_site/anime_list.html'
#         context = super().get_context_data(*args, **kwargs)
#         context["q"] = f'q={self.request.GET.get("q")}&'
#         return context

    # return render(request=request, template_name=self.template_name, context=context)
# https://evileg.com/ru/post/364/