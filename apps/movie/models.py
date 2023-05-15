from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Actor(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Genre(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    rating = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
    genre = models.ManyToManyField(Genre, through="MovieGenre")
    actor = models.ManyToManyField(Actor, through="MovieActor")

    def __str__(self):
        return self.title


class MovieActor(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)

    def __str__(self):
        return self.movie.title


class MovieGenre(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return self.movie.title


class SimilarMovie(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    similar_movie = models.ForeignKey(Movie, related_name="similar_movies", on_delete=models.CASCADE)
