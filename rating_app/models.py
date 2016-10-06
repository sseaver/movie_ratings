from django.db import models

# Create your models here.


class Rater(models.Model):
    age = models.IntegerField()
    gender = models.CharField(max_length=2)
    occupation = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=10)

    def __str__(self):
        return str(self.id)


class Movie(models.Model):
    name = models.CharField(max_length=100)
    date = models.CharField(max_length=20)
    video_release = models.CharField(max_length=20, null=False)
    imdb_url = models.CharField(max_length=100)
    unknown = models.BooleanField()
    action = models.BooleanField()
    adventure = models.BooleanField()
    animation = models.BooleanField()
    childrens = models.BooleanField()
    comedy = models.BooleanField()
    crime = models.BooleanField()
    documentary = models.BooleanField()
    drama = models.BooleanField()
    fantasy = models.BooleanField()
    filmnoir = models.BooleanField()
    horror = models.BooleanField()
    musical = models.BooleanField()
    mystery = models.BooleanField()
    romance = models.BooleanField()
    scifi = models.BooleanField()
    thriller = models.BooleanField()
    war = models.BooleanField()
    western = models.BooleanField()

    def __str__(self):
        return self.name


class Data(models.Model):
    userz = models.ForeignKey(Rater)
    itemz = models.ForeignKey(Movie)
    rating = models.IntegerField()
    timestamp = models.CharField(max_length=20)
