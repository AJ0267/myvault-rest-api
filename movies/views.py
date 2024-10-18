from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MovieSerializer
from .models import MovieData

from rest_framework.decorators import action
from rest_framework.response import Response
import random
# Create your views here.


class MovieViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.all()
    serializer_class = MovieSerializer


    @action(detail=False, methods=['get'], url_path='random')
    def get_random_movie(self, request):
        count = self.queryset.count()
        if count == 0:
            return Response({'message': 'No movies available'}, status=404)
        random_movie = self.queryset[random.randint(0, count - 1)]
        serializer = self.get_serializer(random_movie)
        return Response(serializer.data)