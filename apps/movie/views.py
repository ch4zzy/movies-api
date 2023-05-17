from rest_framework import viewsets

from apps.movie.models import Movie
from apps.movie.serializer import MovieDetailSerializer, MovieListSerializer


class MovieViewSet(viewsets.ModelViewSet):
    """
    Viewset for CRUD operations on Movie model using serializers for list and detail
    """

    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer
        return MovieDetailSerializer
