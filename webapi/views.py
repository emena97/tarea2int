from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Artists, Albums, Tracks
from . serializers import ArtistSerializer, AlbumSerializer, TrackSerializer
from base64 import b64encode


class ArtistList(APIView):
    def get(self, request):
        artistas_l = Artists.objects.all()
        serializer = ArtistSerializer(artistas_l, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        data = request.data
        #chequeamos la data
        try:
            if isinstance(data['name'], str) and isinstance(data['age'], int):
                pass
            else:
                return HttpResponse(status=400)
        except:
            return HttpResponse(status=400)
        check_artist = Artists.objects.filter(name=data['name'])
        try:
            if len(check_artist[0].id) > 0:
                serializer = ArtistSerializer(check_artist[0])
                return Response(serializer.data, status=409)
        except:
            pass
        id_artist = b64encode(data['name'].encode()).decode('utf-8')
        id_artist = id_artist[0:22]
        url_base = 'https://tarea2int.herokuapp.com/artists/'
        albums = url_base + id_artist + '/' + 'albums'
        tracks = url_base + id_artist + '/' + 'tracks'
        self_var = url_base + id_artist
        new_artist = Artists.objects.create(id=id_artist, name=data['name'], age=data["age"], albums=albums, tracks=tracks)
        new_artist.self = self_var
        new_artist.save()
        serializer = ArtistSerializer(new_artist)

        return Response(serializer.data, status=201)


class ArtistID(APIView):
    def get(self, request, id_artist):
        artistas_l = Artists.objects.filter(id=id_artist)
        try:
            if len(artistas_l[0].id) > 0:
                serializer = ArtistSerializer(artistas_l[0], many=True)
                return Response(serializer.data)
        except:
            return HttpResponse(status=404)

    def delete(self, request, id_artist):
        try:
            artists_l = Artists.objects.filter(id=id_artist)
            if len(artists_l[0].id) > 0:
                artists_l[0].delete()
                return HttpResponse(status=204)
        except:
            return HttpResponse(status=404)


class AlbumList(APIView):
    def get(self, request):
        albums_l = Albums.objects.all()
        serializer = AlbumSerializer(albums_l, many=True)
        return Response(serializer.data)


class AlbumID(APIView):
    def get(self, request, id_album):
        albums_l = Albums.objects.filter(id=id_album)
        try:
            if len(albums_l[0].id)>0:
                serializer = AlbumSerializer(albums_l[0], many=True)
                return Response(serializer.data)
        except:
            return HttpResponse(status=404)

    def delete(self, request, id_album):
        try:
            albums_l = Albums.objects.filter(id=id_album)
            if len(albums_l[0].id) > 0:
                albums_l[0].delete()
                return HttpResponse(status=204)
        except:
            return HttpResponse(status=404)


class AlbumPG(APIView):
    def get(self, request, id_artist):
        albums_l = Albums.objects.filter(artist_id=id_artist)
        try:
            if len(albums_l[0].id) > 0:
                serializer = AlbumSerializer(albums_l, many=True)
                return Response(serializer.data)
        except:
            return HttpResponse(status=404)

    def post(self, request, id_artist):
        data = request.data
        # chequeamos la data
        try:
            if isinstance(data['name'], str) and isinstance(data['genre'], str):
                pass
            else:
                return HttpResponse(status=400)
        except:
            return HttpResponse(status=400)
        check_album = Albums.objects.filter(name=data['name'])
        try:
            if len(check_album[0].id) > 0:
                serializer = AlbumSerializer(check_album[0])
                return Response(serializer.data, status=409)
        except:
            pass
        url_base = 'https://tarea2int.herokuapp.com/'
        to_encode = data['name']+':'+id_artist
        album_id = b64encode(to_encode.encode()).decode('utf-8')
        album_id = album_id[0:22]
        artist = url_base+'artists/'+id_artist
        tracks = url_base+'albums/'+album_id+'/tracks'
        self_var = url_base+'albums/'+album_id
        try:
            parent_a = Artists.objects.filter(id=id_artist)[0]
        except:
            return HttpResponse(status=422)
        new_album = Albums.objects.create(id=album_id, artist_id=id_artist, name=data['name'], genre=data["genre"], artist=artist, tracks=tracks, artist_parent=parent_a)
        new_album.self = self_var
        new_album.save()
        serializer = AlbumSerializer(new_album)

        return Response(serializer.data, status=201)


class TrackPG(APIView):
    def get(self, request, id_album):
        tracks_l = Tracks.objects.filter(album_id=id_album)
        try:
            if len(tracks_l[0].id) > 0:
                serializer = TrackSerializer(tracks_l, many=True)
                return Response(serializer.data)
        except:
            return HttpResponse(status=404)

    def post(self, request, id_album):
        data = request.data
        try:
            if isinstance(data['name'], str) and isinstance(data['duration'], float):
                pass
            else:
                return HttpResponse(status=400)
        except:
            return HttpResponse(status=400)
        check_track = Tracks.objects.filter(name=data['name'])
        try:
            if len(check_track[0].id) > 0:
                serializer = TrackSerializer(check_track[0])
                return Response(serializer.data, status=409)
        except:
            pass
        url_base = 'https://tarea2int.herokuapp.com/'
        to_encode = data['name']+':'+id_album
        track_id = b64encode(to_encode.encode()).decode('utf-8')
        track_id = track_id[0:22]
        try:
            a = Albums.objects.filter(id=id_album)
            art_id = a[0].artist_id
        except:
            return HttpResponse(status=422)
        artist = url_base+'artists/'+art_id
        album = url_base+'albums/'+id_album
        self_var = url_base+'tracks/'+track_id
        parent_a = Albums.objects.filter(id=id_album)[0]

        new_track = Tracks.objects.create(id=track_id, album_id=id_album, name=data['name'], duration=data['duration'], times_played=0, artist=artist, album=album, album_parent=parent_a)
        new_track.self = self_var
        new_track.save()
        serializer = TrackSerializer(new_track)

        return Response(serializer.data, status=201)


class TrackList(APIView):
    def get(self, request):
        tracks_l = Tracks.objects.all()
        serializer = TrackSerializer(tracks_l, many=True)
        return Response(serializer.data)


class TracksArtist(APIView):
    def get(self, request, id_artist):
        albums_artista = Albums.objects.filter(artist_id=id_artist)
        try:
            if len(albums_artista[0].id) > 0:
                tracks = Tracks.objects.all()
                tracks_l = []
                for track in tracks:
                    for album in albums_artista:
                        if album.id == track.album_id:
                            tracks_l.append(track)

                serializer = TrackSerializer(tracks_l, many=True)
                return Response(serializer.data)

        except:
            return  HttpResponse(status=404)


class TrackID(APIView):
    def get(self, request, id_track):
        tracks_l = Tracks.objects.filter(id=id_track)
        try:
            if len(tracks_l[0].id) > 0:
                serializer = TrackSerializer(tracks_l[0], many=True)
                return Response(serializer.data)
        except:
            return HttpResponse(status=404)
    def delete(self, request, id_track):
        try:
            tracks_l = Tracks.objects.filter(id=id_track)
            if len(tracks_l[0].id) > 0:
                tracks_l[0].delete()
                return HttpResponse(status=204)
        except:
            return HttpResponse(status=404)


class ArtistPlay(APIView):
    def put(self, request, id_artist):
        try:
            albums_l = Albums.objects.filter(artist_id=id_artist)
            if len(albums_l[0].id) > 0:
                for album in albums_l:
                    tracks = Tracks.objects.filter(album_id=album.id)
                    for track in tracks:
                        track.times_played += 1
                        track.save()
                return HttpResponse(status=200)
        except:
            return HttpResponse(status=404)


class AlbumPlay(APIView):
    def put(self, request, id_album):
        try:
            tracks = Tracks.objects.filter(album_id=id_album)
            if len(tracks[0].id) > 0:
                for track in tracks:
                    track.times_played += 1
                    track.save()
                return HttpResponse(status=200)
        except:
            return HttpResponse(status=404)


class TrackPlay(APIView):
    def put(self, request, id_track):
        try:
            track = Tracks.objects.get(id=id_track)
            if len(track[0].id) > 0:
                track.times_played += 1
                track.save()
                return HttpResponse(status=200)
        except:
            return HttpResponse(status=404)

