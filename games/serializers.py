from rest_framework import serializers
from .models import GameData

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameData
        fields = ['id', 'title', 'genre', 'platform', 'year_of_release']