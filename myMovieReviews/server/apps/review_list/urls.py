from django.urls import path
from server.apps.review_list.views import movie_list, movie_read, movie_create, movie_delete, movie_update

urlpatterns = [
    path("", movie_list),
    path("movie/create", movie_create),
    path("movie/<int:pk>", movie_read),
    path("movie/<int:pk>/update", movie_update),
    path("movie/<int:pk>/delete", movie_delete),
]