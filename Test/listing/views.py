from django.shortcuts import render
from .models import Movie, Genre
import json
from django.http import JsonResponse

# Create your views here.


def loadJsonData(request):
    with open('C:/Users/Siddiq/PycharmProjects/Taks/Test/Test/movies.json', 'r') as f:
        Json_Objects = json.load(f)
    for obj in Json_Objects:

        print("Id  =" + str(obj['id']))
        print("name =" + obj['name'])
        # print("description =" + obj['description'])
        print("Type =" + obj['mpaaRating']['type'])
        print("Lable =" + obj['mpaaRating']['label'])

        movie_instance = Movie.objects.create(movie_id=obj['id'], name=obj['name'], description=obj['description'],
                                              language=obj['language'], mpaaRating_type=obj['mpaaRating']['type'],
                                              mpaaRating_label=obj['mpaaRating']['label'], userRating=int(obj['userRating']),
                                              duration = obj['duration'])
        for g in obj['genre']:
            print("Genra =" + g)
            genre_instance = Genre.objects.create(movie=movie_instance, genre=g)
    return render(request, 'home.html')

def singelMovie(request,movie_id=None):
    movie = Movie.objects.all().get(movie_id=movie_id)
    print(movie)
    movie_detail = {}
    genres = Genre.objects.all().filter(movie=movie)
    movie_detail["name"] = movie.name
    movie_detail["id"] = movie.movie_id
    movie_detail["description"] = movie.description
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

    movies_data = [movie_detail]

    context = {
        'movies': movies_data
    }
    return render(request, 'movieDetail.html',context)

def search_movie(request):
    if is_ajax(request):
        res =None
        searchKeyWord = request.POST.get('searchKeyWord')
        movies = Movie.objects.filter(name__icontains=searchKeyWord)
        print(movies)
        if len(movies) >0 and len(searchKeyWord) >0:
            movies_data = []
            for movie in movies:
                movie_detail = {}
                genres = Genre.objects.all().filter(movie=movie)
                movie_detail["name"] = movie.name
                movie_detail["id"] = movie.movie_id
                movie_detail["duration"] = movie.duration
                movie_detail["image"] = str(movie.imgPath.url)
                movie_detail["language"] = movie.language
                movie_detail["mpaaRating_type"] = movie.mpaaRating_type
                movie_detail["mpaaRating_label"] = movie.mpaaRating_label
                movie_detail["userRating"] = movie.userRating
                gen = []
                for genre in genres:
                    gen.append(genre.genre)
                movie_detail["genre"] = gen
                movies_data.append(movie_detail)
            res = movies_data
        else:
            res = 'No movie found...'
        return JsonResponse({'data' : res})
    return JsonResponse({})

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'