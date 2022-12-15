from django.db import models

# Create your models here.



class Genre(models.Model):
    name = models.CharField('Название', max_length=250)
    url = models.SlugField(max_length=260, unique=True)


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Категория'            #переименование (единственное число)
        verbose_name_plural = 'Категории'     #переименование (множественное число)



class Anime(models.Model):
    title = models.CharField('Название', max_length=250)
    description = models.TextField('Описание', default='')
    poster = models.ImageField('Постер', upload_to='anime_posters/anime_posters')
    genre = models.ManyToManyField(Genre, verbose_name='Жанр')
    pubdate = models.DateField('Дата выхода')
    episodes = models.IntegerField('Эпизодов', default=0)
    url = models.SlugField(max_length=260, unique=True)
    main_picture = models.ImageField('Картинка', upload_to='anime_posters/main_pictures/', default='')
    video_url = models.TextField('Ссылка на аниме', default='')

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Аниме'            #переименование (единственное число)
        verbose_name_plural = 'Аниме'     #переименование (множественное число)