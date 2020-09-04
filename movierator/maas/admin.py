from django.contrib import admin

# Register your models here.
from maas.models.movie import Movie
from maas.models.movie import WatchedList
from maas.models.movie import WatchList

class MovieAdmin(admin.ModelAdmin):
    list_display = ('rank','year','title','rating')
    search_fields = ['title']

admin.site.register(Movie, MovieAdmin)

class WatchListAdmin(admin.ModelAdmin):
    list_display = ('movie_id',)

admin.site.register(WatchList, WatchListAdmin)


class WatchedListAdmin(admin.ModelAdmin):
    list_display = ('movie_id',)

admin.site.register(WatchedList, WatchedListAdmin)