from django.shortcuts import render
from rest_framework import viewsets
from .serializers import GameSerializer
from .models import GameData

from rest_framework.decorators import action
from rest_framework.response import Response
import random
# Create your views here.


class GameViewSet(viewsets.ModelViewSet):
    queryset = GameData.objects.all()
    serializer_class = GameSerializer


    @action(detail=False, methods=['get'], url_path='random')
    def get_random_game(self, request):
        count = self.queryset.count()
        if count == 0:
            return Response({'message': 'No games available'}, status=404)
        random_game = self.queryset[random.randint(0, count - 1)]
        serializer = self.get_serializer(random_game)
        return Response(serializer.data)