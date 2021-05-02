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
        fields = '__all__'


class TrackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tracks
        fields = '__all__'