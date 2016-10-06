from django.contrib import admin
from rating_app.models import Rater, Data, Movie
# Register your models here.

admin.site.register([Rater, Data, Movie])
