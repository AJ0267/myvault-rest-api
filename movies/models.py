from django.db import models

# Create your models here.


class MovieData(models.Model):
    def __str__(self):
        name = self.title
        return name
    
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    cast = models.CharField(max_length=200)
    director = models.CharField(max_length=100)
    year_of_release = models.IntegerField()

