from django.urls import include, path
from rest_framework import routers

app_name = "api_movie"

router = routers.DefaultRouter()
router.register(
    r"movies",
)


urlpatterns = [
    path("", include(router.urls)),
]
