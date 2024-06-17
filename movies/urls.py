from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("movies", views.movies),
    path("movies/<slug:slug>", views.movie_details) #Slugs are short pieces of text, usually written in lowercase letters, stripped of special characters that would be used in the URL of a web page.
]