import json
import random
from datetime import datetime

from django.db import transaction

from apps.movie.models import Actor, Genre, Movie, MovieActor, MovieGenre, SimilarMovie


def load_actors_from_json(file_path):
    """
    Load actor data from a JSON file and save it to the database.
    """
    with open(file_path) as file:
        data = json.load(file)
        for item in data:
            actor = Actor(name=item)
            actor.save()


def load_genre_from_json(file_path):
    """
    Load genre data from a JSON file and save it to the database.
    """
    with open(file_path) as file:
        data = json.load(file)
        for item in data:
            genre = Genre(title=item)
            genre.save()


def load_movies_from_json(file_path):
    """
    Load movie data from a JSON file and save it to the database.
    """
    with open(file_path) as file:
        data = json.load(file)
        for item in data:
            title = item["title"]
            rating = item["rating"]
            genres = item["genres"]
            actors = item["actors"]
            raw_date = item["release_date"]
            try:
                release_date = datetime.strptime(raw_date, "%d %b %Y").date()
                movie = Movie(title=title, rating=rating, release_date=release_date)
                movie.save()
            except ValueError:
                date = raw_date.strip()
                release_date = f"{date}-01-01"
                movie = Movie(title=title, rating=rating, release_date=release_date)
                movie.save()
            for genre_title in genres:
                try:
                    genre = Genre.objects.get(title=genre_title)
                except Genre.DoesNotExist:
                    genre = Genre(title=genre_title)
                    genre.save()

                MovieGenre.objects.create(movie=movie, genre=genre)

            for actor_name in actors:
                try:
                    actor = Actor.objects.get(name=actor_name)
                except Actor.DoesNotExist:
                    actor = Actor(name=actor_name)
                    actor.save()

                MovieActor.objects.create(movie=movie, actor=actor)


def similarity():
    """
    Create random similar movies
    """
    movies = Movie.objects.all()

    with transaction.atomic():
        for movie in movies:
            num_similar_movies = random.randint(1, 2)
            similar_movies = random.sample(list(movies), num_similar_movies)
            for similar_movie in similar_movies:
                SimilarMovie.objects.create(movie=movie, similar_movie=similar_movie)
