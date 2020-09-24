from django.shortcuts import render,get_object_or_404,redirect
from .models import Movie
from common.decorators import login_imp
from taggit.models import Tag
from datetime import date
from django.db.models import Count
from .forms import WriteMovieForm,SearchForm,ReviewForm
from django.http import HttpResponse
from django.contrib.postgres.search import SearchVector
from django.core.paginator import PageNotAnInteger,Paginator, EmptyPage
from django.contrib.auth.models import User
def movie_list(request,genre=None):
    """
    for i in movie:
        i.save()
    """
    #genreFilter
    cat=None
    if genre:
        cat=get_object_or_404(Tag,slug=genre)
        movies=Movie.movies.filter(genre__in=[cat])
    else:
        movies=Movie.movies.all()
    #list View 
    genres=Tag.objects.all()
    paginator=Paginator(movies,10)
    page=request.GET.get('page')
    try:
        movies=paginator.page(page)
    except PageNotAnInteger:
        movies=paginator.page(1)
    except EmptyPage:
        movies=paginator.page(paginator.num_pages)
    #form view
    form=SearchForm()
    query=None
    if 'query' in request.GET:
        form=SearchForm(request.GET)
        if form.is_valid():
            query=form.cleaned_data['query']
            return search_movie(request,query)
    context={'page':page,'movie':movies,'form':form,'genres':genres}
    return render(request,'Movie/list.html',context)
def movie_detail(request,movie):
    movie=get_object_or_404(Movie,slug=movie)
    release_date=movie.release
    genres=Tag.objects.all()
    today=date.today()
    if today>release_date:
        movie.status='Released'
        movie.save()
    movie_gen_id=movie.genre.values_list('id',flat=True)
    similar_movies=Movie.movies.filter(genre__in=movie_gen_id).exclude(id=movie.id)
    similar_movies=similar_movies.annotate(same_genre=Count('genre')).order_by('-same_genre','-rating')[:4]
    new_review=None
    reviews=movie.reviews.all()
    if request.method=='POST':
        r_form=ReviewForm(data=request.POST)
        if r_form.is_valid():
            if request.user.is_authenticated:
                user=request.user
                new_review=r_form.save(commit=False)
                new_review.movie=movie
                new_review.user=user
                new_review.save()
            else:
                return HttpResponse("You need to login first")
    else:
        r_form=ReviewForm()
    context={'movie':movie,'similar_movies':similar_movies,
             'reviews':reviews,'new_review':new_review,
             'r_form':r_form,'genres':genres}
    return render(request,'Movie/detail.html',
                  context)
@login_imp
def write_movie(request):
    if request.method=='POST':
        form=WriteMovieForm(request.POST,request.FILES)
        if form.is_valid():
            movie=Movie()
            movie.title=form.cleaned_data['title']
            movie.director=form.cleaned_data['director']
            movie.starring=form.cleaned_data['starring']
            movie.Plot=form.cleaned_data['plot']
            movie.poster=form.cleaned_data['poster']
            movie.release=form.cleaned_data['release_date']
            genre=form.cleaned_data['genre']
            if not Movie.movies.filter(title=movie.title,release=movie.release).exists():
                movie.save()
                for i in genre:
                    movie.genre.add(i)
                return redirect(movie.get_absolute_url())
            else:
                return HttpResponse('Movie Already exists')
            return redirect(movie.get_absolute_url())
    else:
        form=WriteMovieForm()
    return render(request,'Movie/add_movie.html',
                  {'form':form})
def search_movie(request,query):
    results=Movie.movies.annotate(search=
                                          SearchVector('title','director','starring'),
                                          ).filter(search=query)
    return render(request,'Movie/search.html',
                          {'results':results})