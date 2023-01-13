from django.urls import path
from server.apps.review_list.views import movie_list

urlpatterns = [
    path("", movie_list),
]