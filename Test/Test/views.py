from django.shortcuts import render
import json
from listing.models import Movie , Genre



def home(request):

    movies = Movie.objects.all()
    movies_data = []
    for movie in movies:
        movie_detail = {}
        genres = Genre.objects.all().filter(movie=movie)
        movie_detail["name"] = movie.name
        movie_detail["id"] = movie.movie_id
        movie_detail["duration"] = movie.duration
        movie_detail["image"] = movie.imgPath
        movie_detail["language"] = movie.language
        movie_detail["mpaaRating_type"] = movie.mpaaRating_type
        movie_detail["mpaaRating_label"] = movie.mpaaRating_label
        movie_detail["userRating"] = movie.userRating
        gen = []
        for genre in genres:
            gen.append(genre.genre)
        movie_detail["genre"] = gen
        movies_data.append(movie_detail)


    context = {
        'movies': movies_data
    }
    return render(request, 'home.html',context)



