from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from datetime import date
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
class MovieManager(models.Manager):
    def get_query_set(self):
        return super(MovieManager,self)
def fileuplaod(instance,filename):
        fileformate=filename.split('.')[-1]
        fname=str(instance.slug)+'.'+fileformate
        return 'posters/{}'.format(fname)
class Movie(models.Model):
    title=models.CharField(max_length=250)
    director=models.CharField(max_length=250)
    starring=models.CharField(max_length=500)
    Plot=models.TextField()
    poster=models.ImageField(upload_to=fileuplaod,null=True)
    release=models.DateField()
    status=models.CharField(max_length=10,blank=True)
    slug=models.SlugField(max_length=300,blank=True)
    genre=TaggableManager()
    rating=models.DecimalField(default=0.0,max_digits=2,decimal_places=1)
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify("{obj.title}-{obj.release}".format(obj=self))    
        if not self.status:
            x=date.today()
            if x>self.release:
                self.status='Released'
            else:
                self.status='Upcoming'
        super().save(*args,**kwargs)
    def get_absolute_url(self):
        return reverse('Movie:movie_detail',
                       args=[self.slug])
    class Meta:
        ordering=('-rating',)
    objects=models.Manager()
    movies=MovieManager()
    def __str__(self):
        return self.title
class Reviews(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,
                           related_name='reviews')
    review=models.TextField()
    movie=models.ForeignKey(Movie, on_delete=models.CASCADE,
                            related_name='reviews')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    class Meta:
        ordering=('created',)
    def __str__(self):
        return f'Comment by { self.user } on { self.movie }'