from django.db import models


# Create your models here.

class Movie(models.Model):
    movie_id = models.IntegerField()
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=2000, blank=True)

    imgPath = models.ImageField(upload_to='photos/movie')
    duration = models.IntegerField()

    language = models.CharField(max_length=200,blank=True)
    mpaaRating_type = models.CharField(max_length=200,blank=True)
    mpaaRating_label = models.CharField(max_length=200,blank=True)
    userRating = models.IntegerField()

    def __str__(self):
        return self.name

class Genre(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    genre = models.CharField(max_length=200)







