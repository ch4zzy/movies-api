from django.urls import include, path
from rest_framework import routers

from apps.movie.views import MovieViewSet

app_name = "api_movie"

router = routers.DefaultRouter()
router.register(r"movies", MovieViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
