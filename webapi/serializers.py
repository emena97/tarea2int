from rest_framework import serializers
from . models import Artists, Albums, Tracks
from base64 import b64encode


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artists
        fields = '__all__'


class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Albums
        fields = {'id', 'name', 'genre', 'artist_id', 'artist', 'tracks', 'self'}


class TrackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tracks
        fields = {'id', 'name', 'duration', 'times_played', 'album_id', 'artist', 'album', 'self'}
