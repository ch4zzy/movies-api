from django.contrib import admin

from apps.movie.models import Actor, Genre, Movie, MovieActor, MovieGenre, SimilarMovie


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
    )


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "rating",
        "release_date",
    )


@admin.register(MovieGenre)
class MovieGenreAdmin(admin.ModelAdmin):
    list_display = (
        "movie",
        "genre",
    )


@admin.register(MovieActor)
class MovieActorAdmin(admin.ModelAdmin):
    list_display = (
        "movie",
        "actor",
    )


@admin.register(SimilarMovie)
class SimilarMovieAdmin(admin.ModelAdmin):
    list_display = (
        "movie",
        "similar_movie",
    )
