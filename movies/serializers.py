from rest_framework import serializers
from .models import MovieData

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieData
        fields = ['id', 'title', 'genre', 'cast', 'director', 'year_of_release']