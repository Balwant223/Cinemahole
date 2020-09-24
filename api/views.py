from rest_framework import generics
from Movie.models import Movie,Reviews
from .serializers import MovieSerializer,ReviewSerializer

class MovieListView(generics.ListAPIView):
    queryset=Movie.movies.all()
    serializer_class=MovieSerializer

class MovieDetailView(generics.RetrieveAPIView):
    queryset=Movie.movies.all()
    serializer_class=MovieSerializer

class ReviewListView(generics.ListAPIView):
    queryset=Reviews.objects.all()
    serializer_class=ReviewSerializer

class ReviewDetailView(generics.RetrieveAPIView):
    queryset=Reviews.objects.all()
    serializer_class=ReviewSerializer