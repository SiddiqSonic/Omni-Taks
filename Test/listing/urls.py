from django.urls import path
from . import views


urlpatterns = [
    path('', views.loadJsonData, name='loadjsondata'),
    path('<int:movie_id>/',views.singelMovie,name='singlemovie'),
    path('search/',views.search_movie,name='search_movie'),
]