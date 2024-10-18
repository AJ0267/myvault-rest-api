from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AnimeSerializer
from .models import AnimeData

from rest_framework.decorators import action
from rest_framework.response import Response
import random
# Create your views here.


class AnimeViewSet(viewsets.ModelViewSet):
    queryset = AnimeData.objects.all()
    serializer_class = AnimeSerializer


    @action(detail=False, methods=['get'], url_path='random')
    def get_random_anime(self, request):
        count = self.queryset.count()
        if count == 0:
            return Response({'message': 'No anime available'}, status=404)
        random_anime = self.queryset[random.randint(0, count - 1)]
        serializer = self.get_serializer(random_anime)
        return Response(serializer.data)