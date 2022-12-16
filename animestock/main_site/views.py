from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse
from .models import Anime
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

    
    def get_queryset(self):
        return Anime.objects.filter(title__icontains=self.request.GET.get("q"))


    # def get_context_data(self, *args, **kwargs):
    #     template_name = 'main_site/anime_list.html'
    #     context = super().get_context_data(*args, **kwargs)
    #     context["q"] = self.request.GET.get("q")
    #     return render(request=self.request, template_name=template_name, context=context)    


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = self.request.GET.get("q")
        return render(request=self.request, template_name=template_name, context=context)

    # return render(request=request, template_name=self.template_name, context=context)
# https://evileg.com/ru/post/364/