from django.urls import path
from . import views
app_name='Movie'
urlpatterns=[
    path('',views.movie_list,name='movie_list'),
    path('genre/<slug:genre>',views.movie_list,name="movie_filter"),
    path('add_movie',views.write_movie,name='add_movie'),
    path('<slug:movie>',views.movie_detail,name='movie_detail'),
    path('search',views.search_movie,name='search_movie'),
    ]