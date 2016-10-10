from django.shortcuts import render
# Create your views here.
from rating_app.models import Rater, Movie, Data
from django.db.models import Avg


def index_view(request):
    context = {


    }
    return render(request, "index.html", context)


def top_movie_view(request):
    context = {
        "top_movies": Movie.objects.annotate(top_20=Avg('data__rating')).order_by('-top_20')[:20],


    }
    return render(request, "top_movie.html", context)


def movie_view(request, movie_id):
    context = {
        "movie": Movie.objects.get(id=movie_id),
        "movie_info": Data.objects.filter(itemz=movie_id)
    }
    return render(request, "movie.html", context)


def all_movies_view(request):
    context = {
        "all_movies": Movie.objects.all()

    }
    return render(request, "movies.html", context)


def all_raters_view(request):
    context = {
        "all_raters": Data.objects.all(),


    }
    return render(request, "raters.html", context)


def rater_view(request, rater_id):
    context = {
        "rater": Rater.objects.get(id=rater_id),
        "all_raters": Data.objects.filter(userz=rater_id),
        "rater_info": Rater.objects.filter(id=rater_id)

    }
    return render(request, "rater.html", context)
