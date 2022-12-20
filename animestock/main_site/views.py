from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from .models import Anime, Genre
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
# Create your views here.


#reg/login/logout
def registerPage(request):
    # if request.user.is_authenticated:
    #     # return redirect('/')
    #     pass
    # else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()

                messages.success(request, 'Успешно!')

                return redirect('login')

        context = {'form' : form}
        return render(request, 'register.html', context)
    


def loginPage(request):
    # if request.user.is_authenticated:
    #     # return redirect('/')
    #     pass
    # else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
    
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Имя или Пароль неверны')

        return render(request, 'login.html')


def logoutUser(request):
    logout(request)
    return redirect('index')


# @login_required(login_url='login')
def index(request):
    return render(request, 'index.html')


# @login_required(login_url='login')
def genres(request):
    anime = Anime.objects.all()
    context = {
        'anime' : anime,
    }
    return render(request, 'genres.html', context=context)


# @login_required(login_url='login')
def anime(request):
    return render(request, 'anime.html')


# @login_required(login_url='login')
class Search(ListView):

    model = Anime
    template_name = 'anime_list.html'
 
    def get_queryset(self): # новый
        query = self.request.GET.get('q')
        if query:
            object_list = Anime.objects.filter(
                Q(title__iregex=query) | Q(url__icontains=query)
            )

        else:
            object_list = Anime.objects.all()
       
        return object_list


# @login_required(login_url='login')
class GenreYear:

    def get_genre(self):
        return Genre.objects.all()


    def get_year(self): 
        return Anime.objects.all().values('pubdate')


# а если мы жанр и год выбираем, но при этом у фильма год совпадает, жанр не совпадает то будет выводить  всё равно, потому что одно из условий совпадает, а должно чтобы было логическое "И" при использовании обоих фильтров
# Вот как я сделал, что более правильно работает:
#         if self.request.GET.getlist("genre") and self.request.GET.getlist("year"):
#             queryset = Movie.objects.filter(year__in=self.request.GET.getlist("year"),
#                                             genres__in=self.request.GET.getlist("genre"))
#         else:
#             queryset = Movie.objects.filter(Q(year__in=self.request.GET.getlist("year")) | Q(genres__in=self.request.GET.getlist("genre")))


class Genre(GenreYear):

    def genres(request):
        anime = Anime.objects.all().order_by('id')
        # genres = Genre.ge
        context = {
            'anime_info':anime
        }
        return render(request, 'genres.html', context)


# @login_required(login_url='login')
class AnimeDetail(GenreYear, DetailView):

    model = Anime
    template_name = 'anime_pages/layout_for_anime.html'
    context_object_name = 'anime_page'

    def get(self, request, slug):
        anime = Anime.objects.get(url=slug)
        return render(request, 'anime_pages/layout_for_anime.html', {'anime_page' : anime})



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