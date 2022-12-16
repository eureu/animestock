from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse
from .models import Anime
from django.db.models import Q
# Create your views here.

def index(request):

    search_query = request.GET.get("q")
    if search_query:
        pass

    return render(request, 'index.html')


def genres(request):
    return render(request, 'genres.html')


def anime(request):
    return render(request, 'anime.html')


class Search(ListView):
    model = Anime
    template_name = 'anime_list.html'
 
    def get_queryset(self): # новый
        query = self.request.GET.get('q')
        object_list = Anime.objects.filter(
            Q(title__icontains=query)
        )
        return object_list
    
    # def get_queryset(self):
    #     return Anime.objects.filter(title__icontains=self.request.GET.get("q"))


    

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     context["q"] = f'q={self.request.GET.get("q")}&'
    #     print(context["q"])
    #     print(context)
    #     return context


    # return render(request=request, template_name=self.template_name, context=context)
    # https://evileg.com/ru/post/364/