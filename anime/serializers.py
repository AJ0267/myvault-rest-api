from rest_framework import serializers
from .models import AnimeData

class AnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimeData
        fields = ['id', 'title', 'genre', 'is_movie', 'year_of_release']