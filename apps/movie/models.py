from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Actor(models.Model):
    """
    Model representing an actor
    """

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Genre(models.Model):
    """
    Model representing a genre
    """

    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Movie(models.Model):
    """
    Model representing a movie
    """

    title = models.CharField(max_length=255)
    release_date = models.DateField()
    rating = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
    genre = models.ManyToManyField(Genre, through="MovieGenre")
    actor = models.ManyToManyField(Actor, through="MovieActor")
    similar_movie = models.ManyToManyField("self", through="SimilarMovie", symmetrical=False)

    def __str__(self):
        return self.title


class MovieActor(models.Model):
    """
    Model representing the relationship between a movie and actor
    """

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)

    def __str__(self):
        return self.movie.title


class MovieGenre(models.Model):
    """
    Model representing the relationship between a movie and a genre
    """

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return self.movie.title


class SimilarMovie(models.Model):
    """
    Model representing the relationship between similar movies
    """

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="similar_movies")
    similar_movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.movie.title} - {self.similar_movie.title}"
