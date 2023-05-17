from rest_framework import serializers

from apps.movie.models import Actor, Genre, Movie


class BaseSerializer(serializers.ModelSerializer):
    release_date = serializers.DateField(format="%d-%m-%Y", input_formats=["%d-%m-%Y"])


class GenreSerializer(serializers.ModelSerializer):
    """
    Serializer for Genre model
    """

    class Meta:
        model = Genre
        fields = ("id", "title")


class ActorSerializer(serializers.ModelSerializer):
    """
    Serializer for Actor model
    """

    class Meta:
        model = Actor
        fields = ("id", "name")


class SimilarMovieSerializer(BaseSerializer):
    """
    Serializer for SimilarMovie model
    """

    class Meta:
        model = Movie
        fields = ("title", "release_date")


class MovieListSerializer(serializers.ModelSerializer):
    """
    Serializer for Movie list view
    """

    rating = serializers.DecimalField(max_digits=3, decimal_places=1)
    genre = GenreSerializer(many=True)

    class Meta:
        model = Movie
        fields = ("title", "rating", "genre")


class MovieDetailSerializer(BaseSerializer):
    """
    Serializer for Movie detail view
    """

    genre = GenreSerializer(many=True, read_only=True)
    actor = ActorSerializer(many=True, read_only=True)
    rating = serializers.DecimalField(max_digits=3, decimal_places=1)
    similar_movie = SimilarMovieSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ("title", "release_date", "rating", "genre", "actor", "release_date", "similar_movie")
