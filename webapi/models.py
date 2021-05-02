from django.db import models

# Create your models here.


class Artists(models.Model):
    id = models.CharField(max_length=22, primary_key=True)
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    albums = models.CharField(max_length=300)
    tracks = models.CharField(max_length=300)
    self = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Albums(models.Model):
    id = models.CharField(max_length=22, primary_key=True)
    name = models.CharField(max_length=300)
    genre = models.CharField(max_length=300)
    artist_id = models.CharField(max_length=22)
    artist_parent = models.ForeignKey(Artists, on_delete=models.CASCADE, related_name='+')
    artist = models.CharField(max_length=300)
    tracks = models.CharField(max_length=300)
    self = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Tracks(models.Model):
    id = models.CharField(max_length=22, primary_key=True)
    name = models.CharField(max_length=300)
    duration = models.FloatField()
    times_played = models.IntegerField()
    album_id = models.CharField(max_length=22)
    album_parent = models.ForeignKey(Albums, on_delete=models.CASCADE, related_name='+')
    artist = models.CharField(max_length=300)
    album = models.CharField(max_length=300)
    self = models.CharField(max_length=300)

    def __str__(self):
        return self.name
