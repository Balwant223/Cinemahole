from django import forms
from taggit.forms import *
from .models import Reviews
class WriteMovieForm(forms.Form):
    title=forms.CharField(label='Name')
    director=forms.CharField()
    starring=forms.CharField()
    plot=forms.CharField(widget=forms.Textarea(attrs={'class':'class_plot'}))
    poster=forms.ImageField()
    release_date=forms.DateField()
    genre=TagField()
class SearchForm(forms.Form):
    query=forms.CharField(label="",widget=forms.TextInput
                          (attrs={'placeholder':'Search Movie'}))
class ReviewForm(forms.ModelForm):
    class Meta:
        model=Reviews
        fields=('review',)