from django.urls import path
from . import views

app_name='Movies'

urlpatterns=[
    path('movies/',views.MovieListView.as_view(),name='movie_list'),
    path('movies/<pk>/',views.MovieDetailView.as_view(),name='movie_detail'),
    path('review/',views.ReviewListView.as_view(),name='review_list'),
    path('review/<pk>/',views.ReviewDetailView.as_view(),name='review_detail')
    ]