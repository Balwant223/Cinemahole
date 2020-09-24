from rest_framework import serializers
from Movie.models import Movie,Reviews
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username']
class ReviewSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta:
        model=Reviews
        fields=['review','created','user']
class MovieSerializer(serializers.ModelSerializer):
    reviews=ReviewSerializer(read_only=True)
    class Meta:
        model=Movie
        fields=['id','title','director','rating','reviews']